# Face Recognition

In this project I have only completed the Face Detection part and saving the training data in which we will be using Raspberry Pi.

We have 3 phases in this project
1. [Collecting Training Data](#for-collecting-training-data)
2. [Collecting Testing data](#collecting-testing-data)
3. [Training a model using KNN and predicting](#training-a-model-using-knn-and-predicting)


## For collecting training data
Run trainingDataCreation.py on the Raspberry Pi.
The camera used will be of the phone camera, i.e. IP Webcam app, which can be found on the play store.

### Setting up IP Webcam
- After installing IP webcam in your phone, open it up and scroll down until you see start server.
- After you click it you will see an IP address in the screen with a port number like below i.e. http://192.168.1.102:8080, but this IP would'nt be same for you.

![alt text](https://i1.wp.com/thecodacus.com/wp-content/uploads/2017/07/IP-webcam-android-3.png)


- Note down the IP address and add this extension to it "/shot.jpg", i.e. http://192.168.1.102:8080/shot.jpg.
- Paste the above link in the text file i.e. url_read.txt.
- Before running the code remember that the phone should be on the same network / wifi as the Raspberry Pi / PC.

run: python3 detect_faces_video.py
The above code collects the a set of training data of the students individually and crops out their faces, this training data is saved in the \DATA\train\'name' directory.

## Collecting Testing data
run: python3 collecting_testing_data.py

A set of testing data is created after running the above code in the \DATA\test\'date' directory.

## Training a model using KNN and predicting

run: python3 face_recognition_knn.py
The KNN algorithm is used in the above python file to train the model which was implemented using the Face Recognition API.

Algorithm Description:
The knn classifier is first trained on a set of labeled (known) faces and can then predict the person
in an unknown image by finding the k most similar faces (images with closet face-features under eucledian distance)
in its training set, and performing a majority vote (possibly weighted) on their label.

For example, if k=3, and the three closest face images to the given image in the training set are one image of Biden
and two images of Obama, The result would be 'Obama'.

The installaton of the Face recognition API can be dine by reading the below documentaion.
FaceRecognition API: https://github.com/ageitgey/face_recognition
