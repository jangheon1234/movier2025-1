import pandas as pd

def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[ movies_df['genres'].apply(lambda x: genre in x.lower()) ]
    genre_df = genre_df.fillna('')
    #Todo 선택한 장르의 개수가 5보다 작은 경우 처리해야 함
    result_items = genre_df.sample(n=5).to_dict("records")
    return result_items

# 지정된 장르를 포함하는 영화중 평점이 높은 5개의 영화를 추천함
# def random_genres_items_best(genre):
#     movies_df = pd.read_csv("data/movies_final.csv")
#     rcount_int = movies_df['rcount']
#     rcount = rcount_int.astype(int)
#
#     rcount_df = movies_df[(movies_df['genres'].apply(lambda x: genre in x.lower())) & (rcount >= 5)]
#     genre_df = rcount_df.sort_values(by='rmean', ascending=False)
#
#     genre_df = genre_df.fillna('')
#     result_items = genre_df.head(5).to_dict("records")
#
#     return result_items
# # 2021143016 이장헌
def random_genres_items_best(genre):
    movies_df = pd.read_csv("data/movies_final.csv")

    rcount_int = movies_df['rcount']
    rcount = rcount_int.astype(int)

    rmean_int = movies_df['rmean']
    rmean = rmean_int.astype(float)

    genre_df= movies_df[(movies_df['genres'].apply(lambda x: genre in x.lower())) & (rcount >= 5) & (rmean >= 4.0)]

    if len(genre_df) == 0:
        return []
    genre_df = genre_df.fillna('')

    n_samples = min(5, len(genre_df))
    result_items = genre_df.sample(n=n_samples).to_dict("records")
    return result_items
