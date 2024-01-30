import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

mall_df = pd.read_csv('Mall_Customers.csv')
mall_df.head()
del mall_df['CustomerID']
mall_df['Genre'].replace({'Male':0, 'Female':1}, inplace=True)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d') 

kmeans = KMeans(n_clusters=5)
kmeans.fit(mall_df)



x = mall_df['Age']
y = mall_df['Annual Income (k$)']
z = mall_df['Spending Score (1-100)']
ax.scatter(x, y, z, c = kmeans.labels_, s= 20, alpha=0.5, cmap='rainbow')


plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.show()
