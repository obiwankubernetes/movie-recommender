# importing packages
import pandas as pd

# combining two datasets
ratings_first = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies, ratings_first).drop(['genres','timestamp'],axis=1)

# creating comgined data frame with user id as row, movie title as column and values as the ratings
user_ratings = ratings.pivot_table(index=['userid'), columns=['title'], values=['ratings'])

# remove movies which have les than 10 ratings and put all N/As to 0
user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)

# creqte matrix with userratings and then normalize it
item_similarity_df = user_ratings.corr(method='pearson')

# funtion to get similarity rating
def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings

# testing to see if the recomendations make sense based on giving a few movies some ratings for a sample user profile (romatic lover)
romantic_lover = [("(500) Days of Summer (2009)",5),("Alice in Wonderland (2010)",3),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
similar_movies = pd.DataFrame()
for movie,rating in romantic_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)
# sorting list for romantic lover
similar_movies.sum().sort_values(ascending=False).head(20)

# testing for action lover profile
action_lover = [("Amazing Spider-Man, The (2012)",5),("Mission: Impossible III (2006)",4),("Toy Story 3 (2010)",2),("2 Fast 2 Furious (Fast and the Furious 2, The) (2003)",4)]
similar_movies = pd.DataFrame()
for movie,rating in action_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)
# sorting list for action lover
similar_movies.sum().sort_values(ascending=False).head(20)

