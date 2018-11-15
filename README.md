# FaceRecognition

In this project I have only completed the Face Detection part and saving the training data in which we will be using Raspberry Pi.

1. [Collecting Training Data](#for-collecting-training-data)
2. [Bounding boxes around Faces](#to-run-the-code-in-terminal-run-the-following-command)


## For collecting training data
Run trainingDataCreation.py on the Raspberry Pi.
The camera used will be of the phone camera, i.e. IP Webcam app, which can be found on the play store.

### Setting up IP Webcam
- After installing IP webcam in your phone, open it up and scroll down until you see start server.
- After you click it you will see an IP address in the screen with a port number like below i.e. http://192.168.1.102:8080.

![alt text](https://i1.wp.com/thecodacus.com/wp-content/uploads/2017/07/IP-webcam-android-3.png)


Note down the IP address and paste that in the trainingDataCreation.py on line 12.

Add a new folder of "TRAIN" to run it without errors.



## To run the code in terminal run the following command.

python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel


For now the code draws the bounding box around the face
