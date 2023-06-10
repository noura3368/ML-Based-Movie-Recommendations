# for dataframe
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import quote
import requests

# Data collection and pre-processing 

def get_string_from_df(df, col):
    df_list = df[col].tolist()
    v1 = " ".join(map(str, df_list))
    return v1

def send_api_requests(url, create_dataframe=False, key=''):
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }

    response = requests.get(url, headers=headers).json()
    if create_dataframe:
        df = pd.DataFrame(response[key]) # create df
        return [df, response]
    return response

# loading the data from csv file to pandas df
movies = pd.read_csv('files/movies_metadata.csv', low_memory=False)

selected_features = ['genres', 'keywords', 'tagline', 'director', 'cast']

for feature in selected_features:
    movies[feature] = movies[feature].fillna('')

# combining all the 5 selected features 
combined_features = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['tagline'] + ' ' + movies['director'] + ' ' + movies['cast']

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

else:
    url = "https://api.themoviedb.org/3/search/movie?query=" + quote(movie_name)+ "&page=1"
    found_movie = send_api_requests(url=url)['results'][0]
    
    # get movie deta
    url = "https://api.themoviedb.org/3/movie/"+ str(found_movie['id'])
    movie_details = send_api_requests(url=url, create_dataframe=True, key='genres')
    genres = get_string_from_df(df=movie_details[0], col='name')
    tagline = movie_details[1]['tagline']
    
    # get movie keywords
    url += "/keywords"
    keywords = get_string_from_df(df=movie_details[0], col='name')

    # get the cast from api 
    cast_string = ""
    director = ""
    cast = send_api_requests(url=url.replace('keywords', 'credits'))['cast']
    for c in cast:
        if 'character' in c.keys() and c['character'] != '':
            cast_string += c['original_name'] + " "
        elif 'job' in c.keys() and c['job'] == 'director':
            director += c['name'] + " "
    api_parsed_features = genres + ' ' + keywords + ' ' + tagline + ' ' + director[:-1] + ' ' + cast_string[:-1]

# getting list of similar movies, first val index of movie, second is the similarity score of movie vs inputted movie
similarity_score = sorted(list(enumerate(similarity[index_of_movie])), key = lambda x:x[1], reverse=True)

for index in range(0, 30):
    print(str(index + 1) + ". " + csv_movie_name[similarity_score[index + 1][0]])

