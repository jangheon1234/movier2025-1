import pandas as pd

movies_df = pd.read_csv("movies_final.csv")

movies_df['genres'] = movies_df['genres'].fillna('')  # 결측치 처리
movies_df['split_genres'] = movies_df['genres'].apply(lambda x: x.lower().split('|'))

exploded_df = movies_df.explode('split_genres')

genre_counts = exploded_df['split_genres'].value_counts()

sorted_genres = genre_counts.sort_values(ascending=True)
print("모든 장르의 개수 (적은 순서):")
for genre, count in sorted_genres.items():
    print(f"{genre}: {count}개")
