import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense,Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
sentences=[
    'This is positive sentences',
    'I love this product',
    'This is bad',
    'I hate this experience',
    'Amazing performance',
    'Terrible service'
]
labels=[1,1,0,0,1,0]
vocab_size=1000
embedding_dim=16
max_length=10
trunc_type='post'
padding_type='post'
oov_token='<OOV>'
epochs=10
batch_size=2
tokenizer=Tokenizer(num_words=vocab_size,oov_token=oov_token)
tokenizer.fit_on_texts(sentences)
word_index=tokenizer.word_index
sequences=tokenizer.texts_to_sequences(sentences)
padded_sequences=pad_sequences(sequences,maxlen=max_length,padding=padding_type,truncating=trunc_type)
labels=np.array(labels)
model=Sequential([
    Embedding(vocab_size,embedding_dim,input_length=max_length),
    Bidirectional(LSTM(64,return_sequences=False)),
    Dense(32,activation='relu'),
    Dense(1,activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()
model.fit(padded_sequences,labels,epochs=epochs,batch_size=batch_size)
def predict_sentiment(sentence):
    seq=tokenizer.texts_to_sequences([sentence])
    padded=pad_sequences(seq,maxlen=max_length,padding=padding_type,truncating=trunc_type)
    prediction=model.predict(padded)
    return "Positive" if prediction[0] > 0.5 else "Negative"
new_sentence="I had an amazing time"
print(f"The sentiment for'{new_sentence}' is {predict_sentiment(new_sentence)}")