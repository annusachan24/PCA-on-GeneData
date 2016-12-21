import numpy as np 
import csv
#from sklearn.decomposition import PCA
import collections
from sklearn import decomposition
from matplotlib.mlab import PCA

reader=csv.reader(open("GSE38713_series_matrix_for_GSEA.csv","rb"),delimiter=",")

x=list(reader)
result=np.array(x)
result=np.delete(result,[0],axis=0)
result=np.delete(result,[0,1],axis=1)
result=np.array(result).astype(float)

#result=np.transpose(result)
print result.shape

# ans=PCA(result)
# print type(ans)
# #print ans.shape
# print ans.numrows
# print ans.numcols
# print ans.Y



pca=decomposition.PCA()
# pca.n_components=10000
pca.svd_solver="full"
pca.fit(result)
scores=pca.score_samples(result)
#X_reduced=pca.fit_transform(result)
#X=pca.fit_transform(result)
print scores
print len(scores)

sample_score={}
i=0
pos=0
neg=0
for s in scores:
	if s>=0:
		pos+=1
	else:
		neg+=1
	sample_score[s]=i
	i+=1
sample_score_sorted = collections.OrderedDict(sorted(sample_score.items(),reverse=True))
sorted_samples=sample_score_sorted.values()
best_samples=sorted_samples[0:10000]
print(pca.explained_variance_ratio_) 
print pos, neg
print best_samples
print len(best_samples)
#print len(sample_score_sorted.keys())
#print X[0]


reduced_data=result[best_samples,:]
print reduced_data
print reduced_data.shape
