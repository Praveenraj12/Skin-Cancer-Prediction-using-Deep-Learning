from flask import Flask, render_template, request
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from werkzeug.utils import secure_filename
import numpy as np
import os 
  
'''try:
    import shutil
    shutil.rmtree('uploaded\image')
    print()
except:
    pass'''
  
model = tf.keras.models.load_model('best_model.h5')
app = Flask(__name__)
  
app.config['UPLOAD_FOLDER'] = 'uploaded\image'
  
@app.route('/')
def upload_f():
    return render_template('upload.html')
def finds():
    test_datagen = ImageDataGenerator(rescale = 1./255)
    vals = ['Benign', 'Malignant']
    test_dir = 'uploaded'
    test_generator = test_datagen.flow_from_directory(
            test_dir,
            target_size =(256, 256),
            color_mode ="rgb",
            shuffle = False,
            class_mode ='categorical',
            batch_size = 1)
  
    pred = model.predict_generator(test_generator)
    print(pred)
    return str(vals[np.argmax(pred)])
  
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        val = finds()
        return render_template('pred.html', ss = val)
  
if __name__ == '__main__':
    app.debug= True
    app.run()