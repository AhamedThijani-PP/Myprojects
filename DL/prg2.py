import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
text="Machine Learning is fascinating. Deep learning is a subset of machine learning"
tokenizer=Tokenizer()
tokenizer.fit_on_texts([text])
total_words=len(tokenizer.word_index)+1
input_sequences=[]
for line in text.split('.'):
    token_list=tokenizer.texts_to_sequences([line])[0]
    for i in range(1,len(token_list)):
        n_gram_sequence=token_list[:i+1]
        input_sequences.append(n_gram_sequence)
max_sequence_len=max([len(seq) for seq in input_sequences])
input_sequences=pad_sequences(input_sequences,maxlen=max_sequence_len,padding='pre')
X=input_sequences[:,:-1]
Y=input_sequences[:,-1]
Y=tf.keras.utils.to_categorical(Y,num_classes=total_words)
model=Sequential([
    Embedding(total_words,10,input_length=max_sequence_len-1),
    LSTM(100),
    Dense(total_words,activation='softmax')
])
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=500,verbose=5)
def generated_text(seed_text,next_words,max_sequece_len):
    for _ in range(next_words):
        token_list=tokenizer.texts_to_sequences([seed_text])[0]
        token_list=pad_sequences([token_list],maxlen=max_sequece_len-1,padding='pre')
        predicted=np.argmax(model.predict(token_list,verbose=0),axis=-1)
        output_word=""
        for word,index in tokenizer.word_index.items():
            if index==predicted:
                output_word=word
                break
        seed_text+=""+output_word
    return seed_text
seed_text="Machine Learning"
generated_sentence=generated_text(seed_text,next_words=10,max_sequece_len=max_sequence_len)
print(generated_sentence)