import pandas as pd  
import numpy as np  

dataset = pd.read_csv("banknotes.csv")  
print (dataset.shape)   # Dataset's dimension
print (dataset.head())  # First five entries

# Predictor variables
X = dataset.drop('Class', axis=1)  

# Response variable
y = dataset['Class']  

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  # Train: 80%, Test: 20 % 

# Import the DT Classifier
from sklearn.svm import SVC

# Create Objects
classifier = SVC(kernel='linear')

# Train the algorithm
classifier.fit(X_train, y_train)

# Predict test values
y_pred = classifier.predict(X_test)  

# Import characterizing metrics
from sklearn.metrics import classification_report,      confusion_matrix, accuracy_score  

# Confusion matrix
print (confusion_matrix(y_test, y_pred))

# Print classification report
print (classification_report(y_test, y_pred))

# Accuracy Score
print (accuracy_score(y_test, y_pred) * 100)

from tkinter import *
import tkinter.messagebox
top = Tk()
top.title('Fake Notes Detection System')
top.geometry("500x500")
top.resizable(0, 0) 

window_height = 500
window_width = 900

screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def check():
	global classifier, variance, skewness, curtosis, entropy
	new = np.array([[variance.get(), skewness.get(), curtosis.get(), entropy.get()]])
	print (new)
	y_pred = classifier.predict(new)
	if y_pred[0] == 1:
		tkinter.messagebox.showinfo('Result','NOTE Accepted')
	else:
		tkinter.messagebox.showinfo('Result','NOTE Rejected')

variance = DoubleVar()
skewness = DoubleVar()
curtosis = DoubleVar()
entropy = DoubleVar()

Label(top, text="FAKE NOTES DETECTION SYSTEM", font=('Ubuntu', 25)).place(x=120,y=30)
Label(top, text="Enter variance:", font=('courier', 16)).place(x=20,y=100)
Entry(top, textvariable=variance, font=('courier', 16)).place(x=220,y=100)
Label(top, text="Enter skewness:", font=('courier', 16)).place(x=20,y=150)
Entry(top, textvariable=skewness, font=('courier', 16)).place(x=220,y=150)
Label(top, text="Enter curtosis:", font=('courier', 16)).place(x=20,y=200)
Entry(top, textvariable=curtosis, font=('courier', 16)).place(x=220,y=200)
Label(top, text="Enter entropy", font=('courier', 16)).place(x=20,y=250)
Entry(top, textvariable=entropy, font=('courier', 16)).place(x=220,y=250)
Button(top, text="--Check--", font=('courier', 16, 'bold'), command=check).place(x=220,y=350)

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("rupees.png"))
Label(top, image = img).place(x=500,y=100)
 
top.mainloop()
