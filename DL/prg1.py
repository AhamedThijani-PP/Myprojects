import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN,Dense
text="This is Yenepoya software training institute."
chars=sorted(list(set(text)))
chars_to_index={char:i for i,char in enumerate(chars)}
index_to_chars={i:char for i,char in enumerate(chars)}
seq_length=3
sequences=[]
labels=[]
for i in range(len(text)-seq_length):
    seq=text[i:i+seq_length]
    label=text[i+seq_length]
    sequences.append([chars_to_index[chars] for chars in seq])
    labels.append(chars_to_index[label])
X=np.array(sequences)
Y=np.array(labels)
X_one_hot=tf.one_hot(X,len(chars))
Y_one_hot=tf.one_hot(Y,len(chars))
model=Sequential()
model.add(SimpleRNN(50,input_shape=(seq_length,len(chars)),activation='relu'))
model.add(Dense(len(chars),activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X_one_hot,Y_one_hot,epochs=100,verbose=0)
start_seq="This is Y"
generated_text=start_seq
for i in range(50):
    x=np.array([[chars_to_index[chars] for chars in generated_text[-seq_length:]]])
    x_one_hot=tf.one_hot(x,len(chars))
    prediction=model.predict(x_one_hot)
    next_index=np.argmax(prediction)
    next_char=index_to_chars[next_index]
    generated_text+=next_char
print("Generated Text:")
print(generated_text)