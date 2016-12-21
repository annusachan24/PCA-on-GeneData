import numpy as np 
import csv
from sklearn.decomposition import PCA

reader=csv.reader(open("GSE38713_series_matrix_for_GSEA.csv","rb"),delimiter=",")

x=list(reader)
result=np.array(x)
result=np.delete(result,[0],axis=0)
result=np.delete(result,[0,1],axis=1)
result=np.array(result).astype(float)
#print result[0]
result=np.transpose(result)
print len(result)
print len(result[0])
#in this case n_components == min(n_samples, n_features)
#pca = PCA(n_components=None, copy=True, whiten=False, svd_solver='auto', tol=0.0, random_state=None)
pca=PCA()
#pca = PCA(n_components='mle', copy=True, whiten=False, svd_solver='full', tol=0.0, iterated_power='auto', random_state=None)

X=pca.fit_transform(result)


#print(pca.explained_variance_ratio_) 
#print len(X[0])
#print X[0]


