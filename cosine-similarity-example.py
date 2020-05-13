# finding the similarity/difference between two vectors with words

# install libraries
    # pip install numpy matplotlib pandas scikit-learn gym opencv-python
    # pip show scikit-learn

# load libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# create list of text
text = ["London Paris London", "Paris Paris London"]
# find count of these words (instaead of for loop, use count vectorizer w/in sci-kit learn)
cv = CountVectorizer()
# use fit transform to count the number of vectors in the matrix
count_matrix = cv.fit_transform(text)
# print count_matrix:
    # general print
        # print(count_matrix)
    # print in an array to avoid cordinate representation
        # print(count_matrix.toarray())
# find similarity b/n vectors by passing iniitial text matrix through cosine_similarity
similarity_scores = cosine_similarity(count_matrix)
# print similarity score b/n vectors
print(similarity_scores)


