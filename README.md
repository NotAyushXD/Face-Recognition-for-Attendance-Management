# Face Recognition (The Project is still in progress)

In this project I have only completed the Face Detection part and saving the training data in which we will be using Raspberry Pi.

We have 3 phases in this project
1. [Collecting Training Data](#for-collecting-training-data)
2. [Collecting testing data](#Training a model using KNN and predicting)
3. [Training a model using KNN and predicting](#Training a model using KNN and predicting)


## For collecting training data
Run trainingDataCreation.py on the Raspberry Pi.
The camera used will be of the phone camera, i.e. IP Webcam app, which can be found on the play store.

### Setting up IP Webcam
- After installing IP webcam in your phone, open it up and scroll down until you see start server.
- After you click it you will see an IP address in the screen with a port number like below i.e. http://192.168.1.102:8080, but this IP would'nt be same for you.

![alt text](https://i1.wp.com/thecodacus.com/wp-content/uploads/2017/07/IP-webcam-android-3.png)


- Note down the IP address and add this extension to it "/shot.jpg", i.e. http://192.168.1.102:8080/shot.jpg.
- Paste the above link in the trainingDataCreation.py on line 12.
- Before running the code remember that the phone should be on the same network as the Raspberry Pi / PC.

run: python3 detect_faces_video.py


## Training a model using KNN and predicting

run: python3 collecting_testing_data.py

## Training a model using KNN and predicting

run: python3 face_recognition_knn.py

The reference was taken from the FaceRecgnition API: https://github.com/ageitgey/face_recognition
The installaton of the API is given in the above link


