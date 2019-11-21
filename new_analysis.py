#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 01:09:48 2019

@author: shivam
"""
from nltk import Text 
import nltk
import re


speech_txt = open('ayodhya_verdict_speech_transcript.txt', 'r').read()


type(speech_txt)
len(speech_txt)

speech_txt[:100]

# clean text - removing all punctuations and numbers
speech_txt = re.sub('[^a-zA-Z]', ' ', speech_txt)

# Tokenizations
speech_tokens = nltk.word_tokenize(speech_txt)
type(speech_tokens)
len(speech_tokens)

text = nltk.Text(speech_tokens)
type(text)
text[:100]
len(text)
print(';'.join(text.collocation_list()))

# total words
words = [w for w in text]
vocab = sorted(set(words))

# freq distribution
freq_dist = nltk.FreqDist(words)
freq_dist.plot(50,cumulative=False)

# removing all stop words