import pandas as pd
from fastapi import FastAPI
import uvicorn

from app.data.recommender import item_based_recommendation
from resolver import random_items, random_genres_items, random_genres_items_best

app = FastAPI()

# def random_items():
#     movies_df = pd.read_csv("data/movies_final.csv")
#     movies_df = movies_df.fillna('')
#     result_items = movies_df.sample(n=10).to_dict("records")
#     return result_items

@app.get("/")
async def root():
    return {"message": "Hello MovieR"}

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}

@app.get("/genresbest/{genre}")
async def genre_movies_best(genre: str):
    result = random_genres_items_best(genre)
    return {"result": result}

@app.get("/item_based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)