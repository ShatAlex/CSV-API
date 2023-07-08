# HTTP Servies for working with CSV files

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beautifulsoup4)
![PyPI](https://img.shields.io/pypi/v/beautifulsoup4?label=beautifulsoup4&color=purple)
![PyPI](https://img.shields.io/pypi/v/aiohttp?label=aiohttp&color=yellow)
![PyPI](https://img.shields.io/pypi/v/asyncio?label=asyncio&color=green)

___

### :sparkles: Main information
HTTP service designed to work with imported data in csv format of various formats.

___

### Functionality provided by the API
+ Getting a list of files with information about columns
+ Getting data for a specific file with optional filtering and sorting by columns
+ Implemented user authorization
+ Endpoint for deleting a previously uploaded file
+ A caching system based on Redis has been built
+ Written Dockerfile to run in Docker

___

<center>

    1. Request/Response

</center>
    
<center>

    2.1 Request and response to csv file upload


| Request                                                                                                                                                                                                               | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                             
| curl -X 'POST' \ <br/> 'http://127.0.0.1:8000/files/upload?name=example' \ <br/> -H 'accept: application/json' \ <br/> -H 'Content-Type: multipart/form-data' \ <br/> -F 'file=@dailySteps_merged.csv;type=text/csv' | Response code: 200 <br/> Response body:<br/>{<br/>&nbsp;&nbsp;&nbsp;"status": "success"<br/>} |

</center>

___

<center>

    2.2 Request and response to receive a list of files with information about columns


| Request                                                                                    | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                             
| curl -X 'GET' \ 'http://127.0.0.1:8000/files/review' \ <br/>-H 'accept: application/json' | Response code: 200<br/>Response body:<br/>{<br/>&nbsp;&nbsp;&nbsp;"status": "success", <br/>&nbsp;&nbsp;&nbsp;"data": [<br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"test": [<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logid",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"date"<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br/>&nbsp;&nbsp;&nbsp;&nbsp;],<br/>&nbsp;&nbsp;&nbsp;"details": null<br/>} |

</center>

___

<center>

    2.3 Request and response to receive a specific file



| Request                                                                                                                                                               | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                             
| curl -X 'GET' \ 'http://127.0.0.1:8000/files/get_csv_files/test? <br/> limit=50&offset=0&filter=logid%20%3E%202&order_by=value' \ <br/> -H accept: application/json' | Response code: 200<br/>Response body:<br/>{<br/>&nbsp;&nbsp;&nbsp;"status": "success", <br/>&nbsp;&nbsp;&nbsp;"data": {<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"test": [<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3977333714,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"4/15/2016 10:02:00 AM",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11468101354<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;],<br/>&nbsp;&nbsp;&nbsp;&nbsp;},<br/>&nbsp;&nbsp;&nbsp;"details": null<br/>} |

</center>

___

<center>

    2.4 Request and response to csv file deletion


| Request                                                                                               | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                             
| curl -X 'DELETE' \ <br/> 'http://127.0.0.1:8000/files/example' \ <br/> -H 'accept: application/json' | Response code: 200 <br/> Response body:<br/>{<br/>&nbsp;&nbsp;&nbsp;"status": "success"<br/>} |

</center>

___

### About the project

The service is written in FastAPI with a PostgreSQL database, Redis was used for caching requests.
User authorization is written on the basis of the FastAPI Users library (Cookie, JWT), in the future it is planned to rewrite it to OAuth2.

In the project, it turned out to create a working, but controversial implementation of storing csv files
by dynamically forming the corresponding tables in the database with their content.
For example, since the endpoints are implemented through raw queries to the database, it was not possible to find a working solution on how to connect Celery to the project and had to limit myself to BackgroundTasks.

In general, the API performs the functionality assigned to it.