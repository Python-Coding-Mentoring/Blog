from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# 메인 화면
@app.get('/', tags=['Main'], summary='메인 화면 200 지정')
async def root():
    return JSONResponse(dict(msg='Good'), status_code=200)