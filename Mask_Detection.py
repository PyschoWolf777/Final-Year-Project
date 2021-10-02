import numpy as np
import cv2
from sklearn.svm import SVC
'''
SVM = Support Vector Machine
SVC = Support Vector Classification
'''
from sklearn.metrics import accuracy_score #This will help us to check the accuracy of our algorithm
from sklearn.model_selection import train_test_split #This package is used to select a model for spliting the training and testing data
from sklearn.decomposition import PCA # Used for Dimensionality reduction | PCA = Principal Component Analysis

with_mask = np.load('with_mask.npy') #contains data of 200 pics
without_mask = np.load('without_mask.npy') #contains data of 200 pics
'''
print(with_mask.shape)
print(without_mask.shape)

the output of upper code is

(201, 50, 50, 3)
(201, 50, 50, 3)

as this is 4 dimensional, we convert it into 2 dimensional
'''

with_mask = with_mask.reshape(201, 50*50*3)
without_mask = without_mask.reshape(201, 50*50*3)
'''
print(with_mask.shape)
print(without_mask.shape)

now, the output is

(201, 7500)
(201, 7500)
'''

'''
now as we are going to apply the Machine Learning Algorithm, for which we need features and labels.

so to create a data set. we first combine all the images i.e. with_mask and without_mask in such a way that 
1st 200 will be of with mask and other 200 will be of without mask
'''
X = np.r_[with_mask, without_mask] #this will concatenate the two dataset in sequence-wise

'''
now, 

print(X.shape)

will show the output:
(402, 7500)
'''

#NOW we create label

labels = np.zeros(X.shape[0]) #as X.shape[0] is 402 so this means it will create a array of zeros of size 402 rows each determines each row in X

labels[200:] = 1.0 #Here we have set the last 200 rows's values to 1.0

'''
Now we have created our datasets.
X is features having data of pictures containing mask and without mask
whereas,
labels contains two value 1 or 0.
1 is for wihtout masks
0 is for with masks

now apply ML algo.

Here we are going to use type of CLASSIFICATION which Supervised Learning
This type is of SVM - Support Vector Machine
                SVC - Support Vector Classification
'''

x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size = 0.20) #this model returns both train and both test data
'''
The method,
train_test_split
is used to split your dataset for testing and training.

as we have set 'test_size = 0.25' 
this means 25% of data will be reserved for testing and the rest 75% of data will be used for training
'''

'''
now you data has been splitted. you can verify it by seeing shape of your data like

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

the ouput will be:

(301, 7500)
(101, 7500)
(301,)
(101,)
----------------------------------------------
As there are 7500 columns which are a quite big number, it can create our system slow. so we have to reduce the dimensionality
of the image by using technique of 'DIMENSIONALITY REDUCTION'
For this Purpose we have to import PCA (Principal Component Analysis) form Decomposition pakage of sklearn

This dimentionality Reduction technique use two concepts of mathematics which is 'Eigen Value / Eigen Vector'
'''
pca = PCA(n_components = 3) #in this command upon setting n_components = 3 means we are reducing data to 3 dimension (also our column will be reduced to 3)
x_train = pca.fit_transform(x_train) #this will reduce the x_train data to 3 dimensions (upto 3 columns) and update the x_train variable

'''
print(x_train[0])
print(x_train.shape)

output:
[-2148.13677691    58.0697097    613.33494206]
(301, 3)

now also transform the x_test
'''

x_test = pca.fit_transform(x_test)

#-------------------------------------------------------------
#Now we are going to apply the Machine Learning Algorithm

svm = SVC() #Here the object of svm has created, after that we will use this object

svm.fit(x_train, y_train) #This method is used to train the data

y_predicted = svm.predict(x_test) #this method we make prediction using x_train and y_train and return some labels which we store in y_predicted

#Now ML has been applied, now we will check the accuracy

accuracy = accuracy_score(y_test, y_predicted) #This will check the acurracy between the actual data and predicted

print(accuracy) #if accracy is 1.0 it means it is 100% correct (i.e. accuracy is 100%) which mean the algo is overfit
#100% accuracy is not good for us. so keep re-running or changing the spliting amount in upper 'train_test_split' method to get 90-99 % accuracy

'''
=================================================
Now we apply OpenCV Below

'''
haar_data = cv2.CascadeClassifier('data.xml')
cap = cv2.VideoCapture(0)

data = [] #This List is created to cature the images data

names = {0 : 'With Mask', 1 : 'Without Mask'}

while True:
    ret, frame = cap.read()

    if ret:
        faces = haar_data.detectMultiScale(frame)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 250, 0), 3)
            face = frame[y:y+h, x:x+h, :] #Here it will slice the face portion from the img and store it in face variable
            face = cv2.resize(face, (50, 50))

            #print(face.shape)

            '''
              -1 in reshape function is used when you dont know or want to explicitly tell the dimension of that axis. E.g,
               If you have an array of shape (2,4) then reshaping it with (-1, 1), then the array will get reshaped in such 
               a way that the resulting array has only 1 column and this is only possible by having 8 rows, hence, (8,1).
            '''
            face = face.reshape(1, -1) #so this means it will reduce the array upto only 1 rows and all elements will consider as columns

            face = pca.transform(face)

            #face = pca.fit_transform(face)

            predicts = svm.predict(face)[0]
            n = names[int(predicts)]

            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, n, (x, y), font, 1, (244, 250, 250), 2)

            print(n)


        cv2.imshow("Rsult", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()