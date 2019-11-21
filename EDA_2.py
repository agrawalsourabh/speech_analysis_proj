import nltk

# nltk book download
nltk.download()

from nltk.book import *

print(text1.concordance("monstrous"))

print(text1.similar("monstrous"))

print(text2.common_contexts(["monstrous", "very"]))

a  = 'Hi! How are you? You dumbass'
FreqDist(a)

################################
import nltk
from nltk.corpus import gutenberg

emma = nltk.Text(gutenberg.words('austen-emma.txt'))

num_words = len(gutenberg.words('austen-emma.txt'))
num_words

len(set(gutenberg.words('austen-emma.txt')))

vocab = len(set([w.lower() for w in gutenberg.words('austen-emma.txt')]))

from nltk.corpus import webtext
webtext.fileids()

single = nltk.Text(webtext.words('singles.txt'))
num_words = len(webtext.words('singles.txt'))
num_words

vocab = len(set(webtext.words('singles.txt')))
vocab


# nltk words
from nltk.corpus import words
print(len(words.words()))

# nltk stop words
from nltk.corpus import stopwords
print(len(stopwords.words('english')))

#############################
# words form given letters

puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordList = words.words()

gen_words = [w for w in wordList if len(w) >= 6
             and obligatory in w
             and nltk.FreqDist(w) <= puzzle_letters]

gen_words

len(gen_words)

##################################
# toolbox
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')

##################################
# Exploring wordnet

from nltk.corpus import wordnet as wn
wn.synsets("hello")

print(wn.synset('hello.n.01').lemma_names())

print(wn.synset('hello.n.01').definition())

print(wn.synset('hello.n.01').examples())

wn.synsets("insert")
wn.synset('cut-in.n.02').lemma_names()

wn.synset('cut-in.n.02').definition()