# -*- coding: utf-8 -*-
"""Copy of tf-idf expt

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WuyARBP6rM3x-5lbbj6jGszEt6B2YrHZ
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn import metrics

df=pd.read_json('Sarcasm_Headlines_Dataset.json',lines=True)

data=df[['headline','is_sarcastic']]

tfidf=TfidfVectorizer(sublinear_tf=True,ngram_range=(1,2),stop_words='english')
features = tfidf.fit_transform(df.headline[0:10]).toarray()

tfidf=TfidfVectorizer(sublinear_tf=True,stop_words='english',min_df=3,ngram_range=(1,2))
feature=tfidf.fit_transform(df.headline).todense()

Y=df.is_sarcastic
#Y = np.array(Y).reshape(26709,1,1)

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import Dense, Dropout, Flatten ,LSTM,CuDNNLSTM
from keras.layers import Conv1D,GlobalMaxPool1D,MaxPooling1D
from keras import layers
from keras.utils import np_utils

'''model =Sequential()
model.add(layers.Embedding(vocab_size,128))
model.add(layers.GlobalAveragePooling1D())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 64),
    #tf.keras.layers.Bidirectional(tf.keras.layers.CuDNNLSTM(64)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.summary()
'''

'''
embedding_dim = 64

model = Sequential()
model.add(layers.Embedding(vocab_size, embedding_dim))#, input_length=20000))
model.add(LSTM(embedding_dim, return_sequences=True))
model.add(layers.Conv1D(128, 3, activation='relu'))
model.add(layers.MaxPooling1D(3,strides=2))
#model.add(layers.GlobalAveragePooling1D())
model.add(layers.Conv1D(128, 3, activation='relu'))
model.add(layers.MaxPooling1D(3,strides=2))
#model.add(layers.GlobalAveragePooling1D())
model.add(layers.Conv1D(128, 3, activation='relu'))
model.add(layers.MaxPooling1D(3,strides=2))
model.add(layers.GlobalAveragePooling1D())

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.2))

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.2))

model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(8, activation='relu'))

model.add(layers.Dense(1, activation='sigmoid'))
model.summary()   

model.compile(optimizer='Nadam',
              loss='binary_crossentropy',
              metrics=(['accuracy']))
'''

'''
model.compile(optimizer='adam',
              loss='binary_crossentropy',

              metrics=['acc'])
'''

'''
#model.fit(feature,Y,epochs=5,verbose=1,validation_split=0.2,batch_size=200)
model.fit(feature,Y,epochs=5,verbose=1,
          validation_split=0.2)#,batch_size=200)
'''

Y = np_utils.to_categorical(Y, 2)

Y.shape

model=Sequential()
model.add(Dense(1000,input_shape=(13529,),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(500,activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(50,activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(1,activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',

              metrics=['acc'])

model.fit(feature,Y,epochs=5,verbose=1,
          validation_split=0.2)#,batch_size=200)

