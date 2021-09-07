@myapp.post('/script')
async def startScripts(request: Request):
    try:
        body = await request.json()
        nameScript = 'nameScript'
        paramsScript = "params"

    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body pour executer le / les scripts'})
    except:
        return JSONResponse({'error': 'problème interne'})
    return JSONResponse({'test': 'nous sommes dans les scripts'})
