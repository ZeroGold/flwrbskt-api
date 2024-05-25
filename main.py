from time import time
from fastapi import FastAPI, __version__
#from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,World"


@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
