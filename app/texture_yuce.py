from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import os

norm_size = 208

class texture_rec(object):


    def __init__(self, img_path=None):
        self.img_path = img_path
    
    def load_image(self, img_path):
        self.img_path = img_path

    def predict(self):
        # load the trained convolutional neural network
        print("[INFO] loading network...")
        model = load_model("0613.model")
        
        #load the image
        path=self.img_path
        #print 'path',path
        
        image=cv2.imread(path)
        #cv2.imshow('image',image)
        orig = image.copy()
    
        # pre-process the image for classification
        image = cv2.resize(image, (norm_size, norm_size))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
    
        # classify the input image
        result = model.predict(image)[0]
        result2 = model.predict(image)
        print result2
        #print (result.shape)
    
        proba = np.max(result)
        #proba2=np.array(result)
        #label = str(np.where(result==proba)[0])
        label =(np.where(result==proba)[0])
        #print label[0]
        #print type(label[0])
        
        if label[0]==0:
            label = "{}: {:.2f}%".format("[beach]", proba * 100)
        if label[0]==1:
            label = "{}: {:.2f}%".format("[brick]", proba * 100)
        if label[0]==2:
            label = "{}: {:.2f}%".format("[building]", proba * 100)
        if label[0]==3:
            label = "{}: {:.2f}%".format("[cliff]", proba * 100)
        if label[0]==4:     
            #label2 = str(np.where(result==proba2))
            label = "{}: {:.2f}%".format("[tiles]", proba * 100)
        if label[0]==5:
            label = "{}: {:.2f}%".format("[crack]", proba * 100)
        if label[0]==6:
            label = "{}: {:.2f}%".format("[decal]", proba * 100)
        if label[0]==7:
            label = "{}: {:.2f}%".format("[door]", proba * 100)
        if label[0]==8:
            label = "{}: {:.2f}%".format("[planks]", proba * 100)
        if label[0]==9:
            label = "{}: {:.2f}%".format("[plaster]", proba * 100)
        if label[0]==10:
            label = "{}: {:.2f}%".format("[roofing]", proba * 100)
        if label[0]==11:
            label = "{}: {:.2f}%".format("[window]", proba * 100)
        print(label)
        #print(label2)
        
           
        # draw the label on the image
        output = imutils.resize(orig, width=400)
        cv2.putText(output, label, (10, 25),cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 0, 255), 2)  
        result_path="texture_result.jpg"    
        cv2.imwrite(result_path,output) 

