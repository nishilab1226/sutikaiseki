import sys
import numpy as np
import time
import matplotlib.pyplot as plt
from graph_anime import init,line_init,line_update

import numpy as np

fig,ax = init()

plt.title("time - Matrix_size")
plt.xlabel("Matrix_size")
plt.ylabel("time")
plt.grid()

x = np.zeros(1)
y1 = np.zeros(1)
y2 = np.zeros(1)
line1 = line_init(x,y1,fig,ax,marker="o",label="for")
line2 = line_init(x,y2,fig,ax,marker="^",label="dot")
plt.legend(loc='upper left')

line_update(x,y1,fig,ax,line1)
line_update(x,y2,fig,ax,line2)

for i in range(100,501,100):
	x = np.append(x,i)
	X = np.random.randn(i,i)
	Y = np.random.randn(i,i)
	ans1 = ans2 = np.zeros((i,i))

	start=time.time()
	for i in range(X.shape[0]):
		for j in range(Y.shape[1]):
			#ans[i,j] = np.sum(X[i,:]*Y[:,j])
			ans1[i,j] = sum([x_data*y_data for x_data,y_data in zip(X[i,:],Y[:,j])])
	y1 = np.append(y1,time.time()-start)
	line_update(x,y1,fig,ax,line1)
	#print("for(X,Y) >>> ",ans1)
	print("time = ",time.time()-start)

	start=time.time()
	ans2 = np.dot(X,Y)
	y2 = np.append(y2,time.time()-start)
	line_update(x,y2,fig,ax,line2)
	#print("np.dot(X,Y) >>> ",ans2)
	print("time = ",time.time()-start,"\n")

plt.savefig('mondai1.png')
plt.close()