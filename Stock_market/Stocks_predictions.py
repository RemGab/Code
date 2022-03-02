import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

df=quandl.get('WIKI/AMZN')

df['Prediction']=0

X=np.array(df.drop(['Prediction'],1))
Y=np.array(df['Prediction'])

x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size=0.2)

svr_rbf=SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train,y_train)
#Testing Model Accuracy returns the coefficient of the determination R² of the prediction. The best possible score is 1.0
svm_confidence=svr_rbf.score(x_test,y_test)
print('SVM Confidence', svm_confidence)

LR=LinearRegression()
LR.fit(x_train,y_train)
#Testing Model Accuracy returns the coefficient of the determination R² of the prediction. The best possible score is 1.0
LR_confidence= LR.score(x_test,y_test)
print('SVM Confidenc', LR_confidence)