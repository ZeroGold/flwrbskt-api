from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello_world():
    return "Hello,World"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
