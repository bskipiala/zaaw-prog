import cv2
import numpy as np
import tensorflow as tf

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

label = 'person'

img = cv2.imread('example.jpg')

plt.imshow(img)

