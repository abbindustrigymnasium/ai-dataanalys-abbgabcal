import numpy as np
import cv2
import os

def distance(v1, v2):
    return np.sqrt(((v1-v2)**2).sum())

def knn(train, test, k=5):
    dist = []

    for i in range(train.shape[0]):
        ix = train[i, :-1]
        iy = train[i, -1]
        d = distance(test, ix)
        dist.append([d, iy])
    
    dk = sorted(dist, key=lambda x: x[0])[:k]
    labels = np.array(dk)[:, 1]

    output = np.unique(labels, return_counts=True)

    index = np.argmax(output[1])
    return output[0][index]

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

dataset_path = "./face_data/"

face_data = []
labels = []
class_id = 0
names = {}

for fx in os.listdir(dataset_path):
    