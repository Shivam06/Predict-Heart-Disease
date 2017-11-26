import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.externals import joblib
print("Non-Invasive, Pre-Diagnostic tool for Cardiovascular Diseases\n")
age=input("Age: ")
sex=input("Sex:")
cpt=input("Chest_pain type.")
rest_bp=input("Resting blood pressure (in mm Hg on admission to the hospital)")
chol=input("Cholestoral in mg/dl  ")
fast_sugar=input("Fasting Sugar: ")
rest_ecg=input("Resting ECG: ")
max_hr=input("Maximum heart rate: ")
ex_in=input("Excercise induced angina:")
stdep=input("ST_depression: ")
if(sex=="M"):
	sex = 1
else:
	sex = 0
test = np.zeros((1, 15))
test[0,0]=age
test[0,1]=sex
test[0,2]=rest_bp
test[0,3]=chol
test[0,4]=fast_sugar
test[0,5]=max_hr
test[0,6]=ex_in
test[0,7]=stdep
test[0,7 + int(cpt)]=1
test[0,12 + int(rest_ecg)]=1
test_std = Normalizer().fit_transform(test)
svm_clf=joblib.load('svm.pkl')
y_test_prob = np.array(svm_clf.predict_proba(test_std)[:,1])
print("Your probability of suffering from a heart disease is" + str(y_test_prob[0]))
print("If probability value is greater than 40%, we recommend Angiography.")