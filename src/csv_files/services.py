import csv
import re

from typing import BinaryIO

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_async_session


class CsvFilesService:

    def __init__(self, session: Session = Depends(get_async_session)):
        self.session = session

    async def import_csv(self, tablename: str, file: BinaryIO):

        """ Метод принимает на вход файл, создает
        и наполняет соответствующую таблицу в БД """

        reader = csv.DictReader((line.decode() for line in file))
        headers = reader.fieldnames
        first_row = next(reader, None)
        row_types = []
        if first_row:
            stmt_insert = f'INSERT INTO {tablename} VALUES ('

            for value in first_row.values():
                if value.isdigit():
                    row_types.append('INTEGER')
                    stmt_insert += f'{value}, '
                    continue
                try:
                    float(value)
                    row_types.append('REAL')
                    stmt_insert += f'{value}, '
                    continue
                except Exception:
                    pass
                row_types.append('VARCHAR(255)')
                if value:
                    stmt_insert += f"'{value}', "
                else:
                    stmt_insert += 'Null, '
            for i in range(len(row_types)):
                if re.search('(Id)|(ID)|(id)|(iD)', headers[i]):
                    row_types[i] = 'bigint'
                    continue

            stmt_create = f'CREATE TABLE {tablename} ('
            for i in range(len(row_types)):
                stmt_create += f'{headers[i]} {row_types[i]}, '
            stmt_create = stmt_create[:-2]
            stmt_create += ');'
            stmt_insert = stmt_insert[:-2]
            stmt_insert += ');'
            await self.session.execute(text(stmt_create))
            await self.session.execute(text(stmt_insert))

        for row in reader:
            stmt_insert = f'INSERT INTO {tablename} VALUES ('
            for i, value in enumerate(row.values()):
                if value:
                    if row_types[i] == 'VARCHAR(255)':
                        stmt_insert += f"'{value}', "
                    else:
                        stmt_insert += f'{value}, '
                else:
                    stmt_insert += 'Null, '
            stmt_insert = stmt_insert[:-2]
            stmt_insert += ');'

            await self.session.execute(text(stmt_insert))

        await self.session.commit()

    async def review_csv(self):

        """ Метод возвращает список файлов
            с информацией о колонках """

        query_tables = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' " \
                       "and table_name != 'alembic_version' and table_name != 'user'"
        result = await self.session.execute(text(query_tables))
        tables = [item[0] for item in result.all()]

        data = []

        for table_name in tables:
            query_columns = f"SELECT column_name from information_schema.columns WHERE table_name = '{table_name}'" \
                            "and table_name != 'alembic_version' and table_name != 'user';"
            result = await self.session.execute(text(query_columns))
            columns = [item[0] for item in result.all()]

            data.append({table_name: columns})

        return data

    async def get_csv(self, table_name: str, limit: int, offset: int, filter: str, order_by: str):

        """ Метод возвращает данные из конкретного файла
            с опциональными фильтрацией и сортировкой """

        if filter:
            if order_by:
                query = f"SELECT * FROM {table_name} WHERE {filter} ORDER BY {order_by}"
            else:
                query = f"SELECT * FROM {table_name} WHERE {filter}"
        elif order_by:
            query = f"SELECT * FROM {table_name} ORDER BY {order_by}"
        else:
            query = f"SELECT * FROM {table_name}"
        result = await self.session.execute(text(query))
        result = result.all()
        data = []
        for item in result:
            data.append(list(item))
        return {table_name: data[offset:][:limit]}

    async def drop_csv(self, tablename: str):

        """ Метод удаляет csv файл """

        stmt = f"DROP TABLE {tablename}"
        await self.session.execute(text(stmt))
        await self.session.commit()
