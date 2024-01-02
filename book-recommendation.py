import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('books.csv')
df1 = df.drop(['Unnamed: 12','isbn','isbn13'], axis=1)
#print(df1.head(0))
df2 = df1.loc[(df1['ratings_count']>1000) & (df1['text_reviews_count']>1000)]
#print(df2.info())
#label = LabelEncoder()
#df2['authors'] = label.fit_transform(df2['authors'])
#print(df2['authors'].value_counts())
df2 = df2.drop(['ratings_count','text_reviews_count','publication_date'], axis=1)
list1 = ['title','authors','publisher']
#for i in list1:
def clean_text(author):
    result = str(author).lower()
    return(result.replace(' ',''))

df3 = df2
df2['authors'] = df2['authors'].apply(clean_text)
df2['title'] = df2['title'].apply(clean_text)
df2['publisher'] = df2['publisher'].apply(clean_text)

df2['combined_detail'] = df2['authors']+' '+df2['title']+' '+df2['publisher']
df2 = df2.drop(['authors','title','publisher','  num_pages','average_rating','language_code'], axis=1)
vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df2['combined_detail'])
similarity = cosine_similarity(vectorized)
#print(similarity)
#print(df2.head())
new_df = pd.DataFrame(similarity, columns = df3['title'], index = df3['title']).reset_index()
#print(new_df.head())
input_book = 'harrypotterandthehalf-bloodprince(harrypotter#6)'
recommendations = pd.DataFrame(new_df.nlargest(11,input_book)['title'])
recommendations = recommendations[recommendations['title']!=input_book]
print(recommendations)


