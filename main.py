from typing import Optional

from fastapi import Request, FastAPI
from json import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Test": "Hello World"}


@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})