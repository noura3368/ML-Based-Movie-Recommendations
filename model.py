# for dataframe
import numpy 
import pandas as pd 

import difflib # which movie from dataset is a close match of movie name given 

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

# Data collection and pre-processing 

# loading the data from csv file to pandas df
movies = pd.read_csv('files/movies_metadata.csv', low_memory=False)

# printing the first 5 rows of df
print(movies.head())

# num of rows and cols in dataset
print(movies.shape)