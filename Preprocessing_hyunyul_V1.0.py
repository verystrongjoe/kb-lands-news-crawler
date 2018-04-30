# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:54:47 2018

@author: HyunYul.Choi
"""
# Preprocessing
#전처리는 아래의 세부 과정으로 다시 한 번 나뉜다.
#1. Load text
#2. Tokenize text (ex: stemming, morph analyzing)
#3. Tag tokens (ex: POS, NER)
#4. Token(Feature) selection and/or filter/rank tokens (ex: stopword removal, TF-IDF)
#5. ...and so on (ex: calculate word/document similarities, cluster documents)

## Useful python packages for KoNLPy(provides modules for Korean text Analysis)
# pip install konlpy
# pip install -U gensim
import os
import sys
import csv
import tensorflow as tf
import numpy
import nltk
from konlpy.tag import Twitter; t = Twitter()
from konlpy.corpus import kobill
import pandas as pd
import keras
import keras.backend as K
import pickle
import matplotlib.pyplot as plt


# Set GPU memory usage threshold
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
K.set_session(tf.Session(config=config))

files_ko = kobill.fileids()
doc_ko = kobill.open('naver_news_0425.txt').read()


import konlpy.jvm
konlpy.jvm.init_jvm()

# Tokenize
tokens_ko = t.morphs(doc_ko)


nltk.internals.config_java(options='-xmx50G')


# Load tokens with nltk.Text()
ko = nltk.Text(tokens_ko, name= doc_ko)


print(len(ko.tokens)) #returns num. of tokens (document Length)
print(len(set(ko.tokens))) # returns num. of unique tokens
ko.vocab()                 # returns frequency distribution

# plot frequency distributions
ko.plot(50) # plot sorted frequency of top 50 tokens
# Count
ko.count('규제')
# Dispersion Plot
ko.dispersion_plot(['정부', '완화', '정책'])
# Concordance
ko.concordance('정책')
# Find similar words
ko.similar('강남')
ko.similar('강북')
# Collocations
ko.collocations()

### Tagging and chunking
# 1. POS tagging
tags_ko = t.pos("올해 초 정점을 찍었던 주택매매시장 과열이 입주물량 증가와 맞물리면서 전셋값을 빠른 속도로 끌어내리고 있다.")
# 2. Noun phrase chunking
parser_ko = nltk.RegexpParser("NP: {<Adjective>*<Noun>*}")
chunks_ko = parser_ko.parse(tags_ko)
chunks_ko.draw()
print(ko.vocab())
type(ko.vocab())
dir(ko.vocab())

