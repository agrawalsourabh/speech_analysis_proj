import pandas as pd
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


with open('speech_data.pkl', 'rb') as pickle_file:
    data = pickle.load(pickle_file)

data = pd.DataFrame(data)
print("Before removing puntuactions and numbers: ")
print(data[0][1])

# Cleaning the data

# removing all characters except alphabets
data[0][1] = re.sub('[^a-zA-Z]', ' ', data[0][1])

# change all characters to lower
data[0][1] = data[0][1].lower()

# stopwords and stemming
data[0][1] = data[0][1].split()

ps = PorterStemmer()
data[0][1] = [ps.stem(word) for word in data[0][1] if not word in stopwords.words('english')]

# Joining them completely
data[0][1] = ' '.join(data[0][1])

print(data[0][1])

def to_pickle(data_to_dump, file_name):
    with open(file_name, 'wb') as pickle_file:
        pickle.dump(data_to_dump, pickle_file)
        
to_pickle(data, 'speech_data_clean_1.pkl')

d = [data[0][1]]

# Tokenization
cv = CountVectorizer()
d = cv.fit_transform(d)
d = d.toarray()

data_dtm = pd.DataFrame(d, columns=cv.get_feature_names())
print(data_dtm)

# save it for later use
to_pickle(data_dtm, "data_dtm_clean_1.pkl")

# Importing speech
text = open('ayodhya_verdict_speech_transcript.txt').read()

# SENTIMENT ANALYSIS OF TEXT
import nltk
nltk.download()

from textblob import TextBlob as tb
tb(text).sentiment
