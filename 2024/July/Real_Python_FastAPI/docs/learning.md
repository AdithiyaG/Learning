# Intro
**FastAPI** is the framework you’ll use to build your API, and **Uvicorn** is the server that will use the API you build to serve \
**FastAPI** is built on top of the OpenAPI standard
# Interactive Documentaion

1. Swagger UI \
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. ReDoc UI \
    [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

# First Steps
[first.py](../first.py) wont return anything when you call directly using py.  We need server program uvicorn. \
Run with following cmd

```console
uvicorn <filename>:app --reload
```

with **--reload** parameter we are introducing hot reload functionality.
This creates server in localhost:8000

## Check Response
When you open url in browser, browser sends request to your app,\
then returns response with JSON as
```JSON 
{"message":"Hello World"}
```

> FASTAPI take cares of serializing Python dict into JSON and ContentType

## Explanation of First Steps

1. **FastAPI()** is Python Class provides all functionality to API
2. **app** is instance of FastAPI class
3. **@app.get(/)** is **[Path operation decorator]** decorators tells FastAPI  below function is responsible for handling request coming from corresponding path("\")
   In this case root() will be called by FastAPI whenever  GET request comes to path "/" .
5.  root() is know as **Path operation function**
6. Following HTTP requests can be sent
    * @app.post GET : to read data
    * @app.post() POST: to create data.
    * @app.put() PUT: to update data.
    * @app.delete() DELETE: to delete data.
    * @app.options()
    * @app.head()
    * @app.patch()
    * @app.trace()
      
7. Path operation function can return 
    * dict
    * list
    * singular values like string,int,etc
    * Pydantic models


# Path Parameters

1. you can declare path parameters with python formatted strings
2. In **get_item()** function **item_id** parameter value will be passed to the function

## Path Parameteres with Type Hints
1. You can declare function with hints as **get_item(item_id:int)** will be used for IDE,error checks,completion
### Data Converstion
With Type Hints FastAPI will automatically parse the path parameter to int(In this case).
so for path **item/3** ,you will get response
```JSON
{"item":3}
``` 
> Note: 3 is an integer
### Data Validation

so for path "item/foo" you will get HTTP error.
```JSON
        {
    "detail": [
        {
            "type": "int_parsing",
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "foo"
        }
    ]
}
```
> All the data validation is performed under the hood by pydantic


# Order maters
1. when you decalre two function which handles request for same path 
* function which declared first will handle the request other function will ignored.
* **For Example**:
```python
                                
@app.get("/item/{item_id}")
def get_item2(item_id):
    return {"item":"ntg"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item":item_id}
                              
```
* Here get_item2() will only all get requests from path "/item/{item_id}" get_item will get ignored.

2. similary for paths /user/me & /user/{user_id}
    when function declared first /user/{user_id} before function /user/me. All request for /user/me will be sent to /user/{user_id}, "me" will sent as parameter.









