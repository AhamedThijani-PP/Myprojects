import numpy as np
import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
nltk.download('punkt')
documents=[
    'Deep learning is a subset of machine learning.',
    'Self-Organising maps are a type of neural network.',
    'Natural Language Processing is a field of AI.',
    'Convolutional Networks are used in image processing.',
    'Recurrent Neural Networks work well for sequential data.'
]
vectorizer=TfidfVectorizer()
data=vectorizer.fit_transform(documents).toarray()
map_size=(4,4)
input_dim=data.shape[1]
learning_rate=0.5
epochs=100
weights=tf.Variable(tf.random.normal([map_size[0],map_size[1],input_dim]))
def find_bmu(sample):
    sample=tf.cast(sample,tf.float32)
    expanded_sample=tf.expand_dims(tf.expand_dims(sample,0),0)
    distances=tf.reduce_sum(tf.square(weights-expanded_sample),axis=2)
    bmu_index=tf.argmin(tf.reshape(distances,[-1]))
    bmu_x=bmu_index//map_size[1]
    bmu_y=bmu_index%map_size[1]
    return tf.stack([bmu_x,bmu_y])
for epoch in range(epochs):
    for sample in data:
        sample=tf.cast(sample,tf.float32)
        bmu=find_bmu(sample)
        bmu_x,bmu_y=bmu[0],bmu[1]
for x in range(map_size[0]):
    for y in range(map_size[1]):
        distance=tf.sqrt(tf.cast((bmu_x- x)**2 + (bmu_y-y)**2,tf.float32))
        influence=tf.exp(-distance/(2*learning_rate**2))
        weights[x,y].assign(weights[x,y]+influence*(sample-weights[x,y]))
learning_rate*=0.99
som_map=np.zeros(map_size)
for i,sample in enumerate(data):
    bmu=find_bmu(sample)
    x,y=bmu.numpy()
    som_map[x,y]=i+1
plt.imshow(som_map,cmap='BrBG',interpolation='nearest')
plt.colorbar()
plt.title("Self-Organising Map for Text Data")
plt.show()