import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
import csv

def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        SaveList.append(row)
    return

def storFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

SampleFeature = []
ReadMyCsv(SampleFeature, "CMI/1.csv")



print(len(SampleFeature))
SampleFeature = np.array(SampleFeature)
print('blast',len(SampleFeature))
print('blast[0]',len(SampleFeature[0]))
x = SampleFeature

x_train = SampleFeature
x_test = SampleFeature
x_train = x_train.astype('float32') / 1.
x_test = x_test.astype('float32') / 1.
print(x_train.shape)
print(x_test.shape)
print(type(x_train[0][0]))

input_img = Input(shape=(len(SampleFeature[0]),))

from keras import regularizers
encoded_input = Input(shape=(encoding_dim,))
encoded = Dense(encoding_dim, activation='relu', activity_regularizer=regularizers.l1(10e-5))(input_img)
decoded = Dense(3308, activation='sigmoid')(encoded)

autoencoder = Model(inputs=input_img, outputs=decoded)
decoder_layer = autoencoder.layers[-1]
encoder = Model(inputs=input_img, outputs=encoded)
decoder = Model(inputs=encoded_input, outputs=decoder_layer(encoded_input))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
autoencoder.fit(x_train, x_train, epochs=10, batch_size=50, shuffle=True, validation_data=(x_test, x_test))

encoded_imgs = encoder.predict(x)
decoded_imgs = decoder.predict(encoded_imgs)
print(len(encoded_imgs))
print(len(encoded_imgs[1]))
storFile(encoded_imgs, 'CMI/2.CSV')