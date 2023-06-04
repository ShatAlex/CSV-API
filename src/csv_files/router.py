from typing import Optional

from fastapi import APIRouter, UploadFile, File, Depends
from fastapi_cache.decorator import cache
from starlette.background import BackgroundTasks

from csv_files.services import CsvFilesService

router_files = APIRouter(
    prefix='/files',
    tags=['Files']
)


@router_files.post('/upload')
def upload_csv(name: str, bg_task: BackgroundTasks, file: UploadFile = File(...),
               csv_files_service: CsvFilesService = Depends()):
    bg_task.add_task(csv_files_service.import_csv, name, file.file)
    return {"status": "success"}


@router_files.get('/get_csv_files/{table_name}')
@cache(expire=600)
async def review_csv(table_name: str, limit: int = 50, offset: int = 0, filter: Optional[str] = None,
                     order_by: Optional[str] = None, csv_files_service: CsvFilesService = Depends()):
    data = await csv_files_service.get_csv(table_name, limit, offset, filter, order_by)
    return {
        'status': 'success',
        'data': data,
        'details': None
    }


@router_files.get('/review')
@cache(expire=600)
async def review_csv(csv_files_service: CsvFilesService = Depends()):
    data = await csv_files_service.review_csv()
    return {
        'status': 'success',
        'data': data,
        'details': None
    }


@router_files.delete('/{table_name}')
async def delete_csv(table_name: str, csv_files_service: CsvFilesService = Depends()):
    await csv_files_service.drop_csv(table_name)
    return {"status": "success"}
