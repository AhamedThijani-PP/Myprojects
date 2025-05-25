import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
(train_images,_),(_,_)=keras.datasets.mnist.load_data()
train_images = train_images.reshape(-1,28,28,1).astype('float32')/127.5-1
latent_dim=100
batch_size=128
epochs=1000
def build_generator():
    model=keras.Sequential([
        layers.Dense(128,activation='relu',input_shape=(latent_dim,)),
        layers.Dense(256,activation='relu'),
        layers.Dense(28*28*1,activation='tanh'),
        layers.Reshape((28,28,1))
    ])
    return model
def build_descriminator():
    model=keras.Sequential([
        layers.Flatten(input_shape=(28,28,1)),
        layers.Dense(256,activation='relu'),
        layers.Dense(128,activation='relu'),
        layers.Dense(1,activation='sigmoid')
    ])
    return model
generator=build_generator()
discriminator=build_descriminator()
discriminator.compile(loss='binary_crossentropy',optimizer=keras.optimizers.Adam(),metrics=['accuracy'])
discriminator.trainable=False
gan_input=keras.Input(shape=(latent_dim,))
gan_output=discriminator(generator(gan_input))
gan=keras.Model(gan_input,gan_output)
gan.compile(loss='binary_crossentropy',optimizer=keras.optimizers.Adam())
def train_gan():
    for epoch in range(epochs):
        noise=np.random.normal(0,1,(batch_size,latent_dim))
        generated_images=generator.predict(noise)
        real_images=train_images[np.random.randint(0,train_images.shape[0],batch_size)]
        labels_real=np.ones((batch_size,1))
        labels_fake=np.ones((batch_size,1))
        d_loss_real=discriminator.train_on_batch(real_images,labels_real)
        d_loss_fake=discriminator.train_on_batch(generated_images,labels_fake)
        d_loss=0.5*np.add(d_loss_real,d_loss_fake)
        noise=np.random.normal(0,1,(batch_size,latent_dim))
        label_gan=np.ones((batch_size,1))
        g_loss=gan.train_on_batch(noise,label_gan)
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, D Loss: {d_loss[0]},G Loss: {g_loss}")
            generate_and_save_images(epoch)
def generate_and_save_images(epoch):
    noise=np.random.normal(0,1,(16,latent_dim))
    generated_images=generator.predict(noise)
    generated_images=(generated_images+1)/2
    fig,axes=plt.subplots(4,4,figsize=(4,4))
    for i,ax in enumerate(axes.flat):
        ax.imshow(generated_images[i,:,:,0],cmap='gray')
        ax.axis('off')
    plt.savefig(f'gan_image_epoch_{epoch}.png')
    plt.close()
train_gan()
