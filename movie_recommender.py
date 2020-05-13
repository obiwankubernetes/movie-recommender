# tutorial @ https://youtu.be/XoTwndOgXBM

# install packages

# load packages
from pandas import DataFrame, read_csv
import numpy 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


##Step 1: Read CSV File
# define dataframe format and file
df = pandas.read_csv("imdb-movie-data.csv")
# print
# print(df)

##Step 2: Select Features
# define list of features we want under a variable 
# keywords in synopsis, cast, genre, and director probably predict a similar movie you would like
fearures = ['keywords','cast','genre','director']
# fill any n/as with an empty string
for feature in features:
	df[feature] = df[feature]:fillna{''}

##Step 3: Create a column in DF which combines all selected features (words) into one string
# helper function to get one string with all features
def combine_features(row):
	try:
		return row['keywords'] + " " + row["cast"] + " " + row["genres"] + row["director"]
	except:
		print("Error:", row)
# now use this function on every row and put in seperate columgn
df["combined_features"] = df.apply(combine_features, axis=1)

##Step 4: Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
similarity_scores = cosine_similarity(count_matrix)

## Step 6: Get index of movie user likes from its title
# define example movie user like
movie_user_likes = "Avatar"
# define function to get index number of movie in csv (row #) from title
def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
#pull index number for avatar
movie_index = get_index_from_title(movie_user_likes)

## Step 7: Get a list of similar movies in descending order of similarity score
# get list (unsorted)
similar_movies = list(enumerate(similarity_scores[movie_index]))
# sort list in descending order of similiarity
sorted_similar_movies = sorted(similar_movies, key=Lamdba x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
# define function to pull title of movie from index:
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]
# define for lopp to get movie titles from the sorted list
for movie in sorted_similar_movies:
	print get_title_from_index(movie[0])
	i=i+1
	if i>50:
		break
