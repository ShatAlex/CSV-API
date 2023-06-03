from celery import Task
from fastapi import Depends

from csv_files.services import CsvFilesService


class CustomTask(Task):
    ignore_result = True

    def __init__(self, tablename, file):
        self.tablename = tablename
        self.file = file

    async def run(self, csv_files_service: CsvFilesService = Depends()):
        await csv_files_service.import_csv(self.tablename, self.file)
