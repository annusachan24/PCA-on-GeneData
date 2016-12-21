import numpy as np 
import csv
#from sklearn.decomposition import PCA
import collections
from sklearn import decomposition
from matplotlib.mlab import PCA

reader=csv.reader(open("GSE38713_series_matrix_for_GSEA.csv","rb"),delimiter=",")

x=list(reader)

#converting into numpy array for processing
result=np.array(x)

#storing headers,names and description to be written into output file before removing it from result array
header=result[0,:]
names=result[:,0]

#removing the first row of cvs and first 2 coulmns which will not be used in PCA
result=np.delete(result,[0],axis=0)
result=np.delete(result,[0,1],axis=1)

#converting to float
result=np.array(result).astype(float)


#applying pca with n_components=None
pca=decomposition.PCA()
pca.svd_solver="full"
pca.fit(result)
scores=pca.score_samples(result)

#storing the scores of each sample (Log-likelihood of each sample under the current model)
#sort the samples based on their score and take the best 10000 as per the requirement

sample_score={}
i=0
for s in scores:
	sample_score[s]=i
	i+=1
sample_score_sorted = collections.OrderedDict(sorted(sample_score.items(),reverse=True))
sorted_samples=sample_score_sorted.values()
best_samples=sorted_samples[0:10000]



reduced_data=result[best_samples,:]
reduced_data=reduced_data.tolist()

#adding first and second column
ind_to_name=0
for r in reduced_data:
	r.insert(0,'NA')
	r.insert(0,names[best_samples[ind_to_name]])
	ind_to_name+=1




#creating the output csv file
with open('reduced_data.csv','w') as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerow(header)
	ind=0
	for row in reduced_data:
		writer.writerow(row)
		ind+=1
print header
print "data successfully written to file"
