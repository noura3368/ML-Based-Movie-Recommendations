# for dataframe
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

# Data collection and pre-processing 

# loading the data from csv file to pandas df
movies = pd.read_csv('files/movies_metadata.csv', low_memory=False)
# num of rows and cols in dataset
#print(movies.shape)

selected_features = ['genres', 'keywords', 'tagline', 'director', 'cast']

for feature in selected_features:
    movies[feature] = movies[feature].fillna('')

# combining all the 5 selected features 
combined_features = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['tagline'] + ' ' + movies['director'] + ' ' + movies['cast']
#print(combined_features)

# converting text to feature vector/converting to numerical value to cosine value
vectorizer = TfidfVectorizer()

features = vectorizer.fit_transform(combined_features) # creating a numerical val of combined features

# find similarity score using cosine similarity
similarity = cosine_similarity(features)

movie_name = input("Enter favourite movie name: ").lower()

csv_movie_name = list(map(str.lower, list(movies['title'])))

# finding a recommendation based off of movie given from user
if movie_name in csv_movie_name:
    index_of_movie = csv_movie_name.index(movie_name)
    print(index_of_movie)

# getting list of similar movies, first val index of movie, second is the similarity score of movie vs inputted movie
similarity_score = sorted(list(enumerate(similarity[index_of_movie])), key = lambda x:x[1], reverse=True)

for index in range(0, 30):
    print(str(index + 1) + ". " + csv_movie_name[similarity_score[index + 1][0]])

