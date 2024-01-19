# for dataframe
import pandas as pd 
import os
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import quote
import requests
import sys
from pymongo import MongoClient

def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        #mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        mongo_uri = "mongodb+srv://" + username + ":" + password + "@atlascluster.dybfxzl.mongodb.net/?retryWrites=true&w=majority&authSource=admin&connectTimeoutMS=60000"
        conn = MongoClient(mongo_uri, connect=False)
    else:
        conn = MongoClient(host, port, connect=False)
    return conn[db]

def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    #print(cursor)
    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))
    
    # Delete the _id
    if no_id:
        del df['_id']

    return df, db[collection]

# Data collection and pre-processing 
def get_string_from_df(df, col):
    df_list = df[col].tolist()
    v1 = " ".join(map(str, df_list))
    return v1

def send_api_requests(url, create_dataframe=False, key=''):
    headers = {
        "accept": "application/json",
        'Authorization': 'Bearer ' + str(sys.argv[2])
        }

    response = requests.get(url, headers=headers).json()
    if create_dataframe:
        df = pd.DataFrame(response[key]) # create df
        return [df, response]
    return response

def return_lower_case_title(title):
    return str(title).lower()

# loading the data from csv file to pandas df
def main(movie_name=""):
    movies, collection_value = read_mongo(db="movieData", collection="movies", username="noura3368", password=sys.argv[3])
    csv_movie_name = []
    csv_movie_poster = []
    for index, row in movies.iterrows(): 
        csv_movie_name.append(return_lower_case_title(row['title'])) 
        csv_movie_poster.append(row['poster_path'])
    # finding a recommendation based off of movie given from user
    if movie_name in csv_movie_name:
        index_of_movie = csv_movie_name.index(movie_name)

    else:
        url = "https://api.themoviedb.org/3/search/movie?query=" + quote(movie_name)+ "&page=1"
        found_movie = send_api_requests(url=url)['results'][0]
        # get movie data
        url = "https://api.themoviedb.org/3/movie/"+ str(found_movie['id'])
        movie_details = send_api_requests(url=url, create_dataframe=True, key='genres')
        genres = get_string_from_df(df=movie_details[0], col='name')
        
        # get movie keywords
        url += "/keywords"
        keywords = get_string_from_df(df=send_api_requests(url=url, create_dataframe=True, key='keywords')[0], col='name')

        dictionary_of_new_row_movie = {"genres": genres, "keywords": keywords, "title": found_movie['original_title'], "poster_path":found_movie["poster_path"]}
        if str(found_movie['original_title']).lower() not in csv_movie_name:
            new_row_from_user = pd.DataFrame([dictionary_of_new_row_movie])
            api_parsed_features = genres + ' ' + keywords 
            movies = pd.concat([new_row_from_user, movies.loc[:]]).reset_index(drop=True)
            index_of_movie = 0
            collection_value.insert_one(dictionary_of_new_row_movie)
        else:
            index_of_movie = csv_movie_name.index(str(found_movie['original_title'].lower()))
        #collection_value.insert_one({"genres": genres, "keywords":keywords, "original_title":movie_name, "title":movie_name})

    selected_features = ['genres', 'keywords']

    for feature in selected_features:
        movies[feature] = movies[feature].fillna('')

    # combining all the 5 selected features 
    combined_features = movies['genres'] + ' ' + movies['keywords'] 
    # converting text to feature vector/converting to numerical value to cosine value
    vectorizer = TfidfVectorizer()

    features = vectorizer.fit_transform(combined_features) # creating a numerical val of combined features

    # find similarity score using cosine similarity
    similarity = cosine_similarity(features)
    # getting list of similar movies, first val index of movie, second is the similarity score of movie vs inputted movie
    similarity_score = sorted(list(enumerate(similarity[index_of_movie])), key = lambda x:x[1], reverse=True)
    movie_rec_dict = {}
  
    for index in range(0, 21):  
        movie_rec_dict[csv_movie_name[similarity_score[index + 1][0]]] = "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + csv_movie_poster[similarity_score[index + 1][0]]
    print(movie_rec_dict)
    #sys.stdout.flush()

main(movie_name=return_lower_case_title(sys.argv[1]))