import cv2
from glob import glob
import numpy
from time import time
import collections



def drawboxesonimg(classidx, confdraw, boxdraw, imgdraw):
    for classIndex, confidence, boxes in \
            zip(classidx.flatten(), confdraw.flatten(), boxdraw):
        if classIndex == 1:
            cv2.rectangle(imgdraw, boxes, (0, 255, 0), 3)
            cv2.putText(
                imgdraw,
                classLabels[classIndex - 1],
                (boxes[0] + 10, boxes[1] + 40),
                cv2.FONT_HERSHEY_COMPLEX,
                fontScale=0.8,
                color=(128, 0, 255),
                thickness=2
            )


configFile = 'model/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozenModel = 'model/frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozenModel, configFile)
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

threshold = 0.57

imgPath = glob("images/*.jpg")
fileName = 'model/labels.txt'
with open(fileName, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

for img in imgPath:
    image = cv2.imread(img)
    originalImage = cv2.imread(img)
    start_time = time()
    classIdx, conf, box = model.detect(image, threshold)
    timeElapsed = time() - start_time
    drawboxesonimg(classIdx, conf, box, image)
    viewImg = numpy.vstack((image, originalImage))
    personCount = collections.Counter(numpy.array(classIdx))[1]
    personText = f"Na zdjeciu znajduje sie {personCount} osob."
    timeText = f"Czas rozpoznania: {round(timeElapsed, 5)} sekund."
    print(personText)
    print(timeText)
    titleWindow = f"{personText} {timeText}"
    cv2.imshow(titleWindow, viewImg)
    cv2.waitKey()
    cv2.destroyWindow(titleWindow)
