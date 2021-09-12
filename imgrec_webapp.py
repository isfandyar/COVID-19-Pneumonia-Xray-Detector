import os 
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

from keras.models import load_model 
from keras.backend import set_session
from skimage.transform import resize 
import matplotlib.pyplot as plt 
import tensorflow as tf 
import numpy as np 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
warnings.filterwarnings("ignore")
import os
import shutil
import matplotlib.pyplot as plt
%matplotlib inline
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.callbacks import EarlyStopping

import pickle
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image


from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

import tensorflow as tf
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator,array_to_img

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten

print("Loading model") 
global sess
sess = tf.Session()
set_session(sess)
global model 
model = load_model('CNN_model_3.h5') 
global graph
graph = tf.get_default_graph()

@app.route('/', methods=['GET', 'POST']) 
def main_page():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        return redirect(url_for('prediction', filename=filename))
    return render_template('index.html')

@app.route('/prediction/<filename>') 
def prediction(filename):
    #Step 1
    my_image = plt.imread(os.path.join('uploads', filename))
    #Step 2
    my_image_re = resize(my_image, (224,224))
    x = image.img_to_array(my_image_re)
    x = np.expand_dims(x, axis =0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size = 32)
    predictedClass = np.argmax(classes, axis=1)
    predictedClass = np.vectorize(dict.get)(predictedClass)
    
    dict = {0: 'COVID-19 PNEUMONIA', 
        1: 'NORMAL', 
        2: 'OTHER PNEUMONIA'}

    #Step 3
    with graph.as_default():
      set_session(sess)
      classes = model.predict(images, batch_size = 32)
      predictedClass = np.argmax(classes, axis=1)
      predictedClass = np.vectorize(dict.get)(predictedClass)
      print(classes)
      #Step 4
      number_to_class = ['COVID-19 PNEUMONIA', 'NORMAL', 'OTHER PNEUMONIA']
      index = np.argsort(classes)
      predictions = {
        "class1":number_to_class[index[9]],
        "class2":number_to_class[index[8]],
        "class3":number_to_class[index[7]],
        "prob1":classes[index[9]],
        "prob2":classes[index[8]],
        "prob3":classes[index[7]],
      }
    #Step 5
    return render_template('predict.html', predictions=predictions)

app.run(host='0.0.0.0', port=80)
