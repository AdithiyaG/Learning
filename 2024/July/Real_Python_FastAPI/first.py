from fastapi import FastAPI

#First Steps

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


#Path Parameters

# @app.get("/item/{item_id}")
# def get_item(item_id):
#     return {"item":"ntg"}

#Path Parameters with type hints

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item":item_id}

