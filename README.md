# FaceRecognition

In this project I have only completed the Face Detection part and saving the training data in which we will be using Raspberry Pi.

## For collecting training data
Run trainingDataCreation.py on the Raspberry Pi.
The camera used will be of the phone camera, i.e. IP Webcam app on the playstore.


Add a new folder of "TRAIN" to run it without errors.



## To run the code in terminal run the following command.

python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel


For now the code draws the bounding box around the face
