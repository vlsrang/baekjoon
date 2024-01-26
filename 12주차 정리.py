f=open("economy.csv",'w')
cri=['tradeprice_sido_n1','date,region_cd','tradeprice_sido','year',\
     'month','building_type','construction_realized_amount','cd','spirit_deposit_rate',\
     'exchange_rate','composite_stock_price_index','economy_growth',\
     'exchequer_bond_three','household_loan_all','mortgage_all','numberofnosells','unsalenum_c']


##### library import #####
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 밑에는 선택 알고리즘
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd

# 분류용 샘플 데이터 불러오기
news = fetch_20newsgroups()
X,y,labels = news.data, news.target, news.target_names

newsdata=fetch_20newsgroups(subset='train')
newsdata_test = fetch_20newsgroups(subset='test', shuffle=True)

# 학습/테스트 데이터셋 분할 
X_train, X_test,y_train,y_test=train_test_split(news.data, news.target,test_size=0.3,random_state=1,stratify=y)

# 데이터 전처리(벡터화)
vectorizer=CountVectorizer()
tfid=TfidfTransformer()
X_train_vec=vectorizer.fit_transform(X_train)
X_test_vec=vectorizer.transform(X_test)
X_train_tfid=tfid.fit_transform(X_train_vec)
X_test_tfid=tfid.transform(X_test_vec)


# 다중분류 나이브 베이즈
mod = MultinomialNB()
mod.fit(X_train_tfid, y_train)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
predicted = mod.predict(X_test_tfid)


#### do not edit here ####
report = classification_report(y_true = y_test, y_pred = predicted)
print('Topic 분류 결과:')
print(report)
---------------------------------------------------------------

import pandas as pd
import matplotlib
import sklearn
from sklearn.linear_model import LinearRegression

ge = pd.read_csv("economy.csv", parse_dates =["date"], index_col ="date")
ge = ge.dropna()
train = ge[(ge.year > 2006) & (ge.year < 2017)]
test = ge[ge.year >= 2017]

feature_names = ['region_cd', 'year', 'month', 'building_type',
                 'tradeprice_sido', 'construction_realized_amount','cd',
                 'spirit_deposit_rate','exchange_rate','composite_stock_price_index',
                 'economy_growth','exchequer_bond_three','household_loan_all',
                 'mortgage_all','numberofnosells','unsalenum_c']


X_train = train[feature_names]
X_test = test[feature_names]

lable_name = "tradeprice_sido_n1"
Y_train = train[lable_name]
Y_test = test[lable_name]

lm = LinearRegression(fit_intercept=True, normalize=True, n_jobs=None)
lm.fit(X_train, Y_train)
accuracy = lm.score(X_test, Y_test)


print ('Linear Regression test file accuracy:'+str(accuracy))


import matplotlib.pyplot as plt
Y_pred = lm.predict(X_test)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Price Index: $Y_i$")
plt.ylabel("Predicted price Index: $\hat{Y}_i$")
plt.title("Prices vs Predicted price Index: $Y_i$ vs $\hat{Y}_i$")
