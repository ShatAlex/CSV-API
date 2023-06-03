from typing import Optional

from fastapi import APIRouter, UploadFile, File, Depends
from fastapi_cache.decorator import cache
from csv_files.services import CsvFilesService
from tasks import CustomTask

router_files = APIRouter(
    prefix='/files',
    tags=['Files']
)


@router_files.post('/upload')
async def upload_csv(name: str, file: UploadFile = File(...), csv_files_service: CsvFilesService = Depends()):
    # custom_task = CustomTask(name, file.file)
    # custom_task.delay()
    # csvFilesService_wrapper.delay(name, file.file)
    # await csv_files_service.import_csv(name, file.file)
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
async def delete_gamemode(table_name: str, csv_files_service: CsvFilesService = Depends()):
    await csv_files_service.drop_csv(table_name)
    return {"status": "success"}
