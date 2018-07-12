import numpy as np
import time
import matplotlib.pyplot as plt

import numpy as np

plt.title("time - Matrix_size")
plt.xlabel("Matrix_size")
plt.ylabel("time")
plt.grid()

x = np.array([])
y1 = np.array([])
y2 = np.array([])

for i in range(100,501,100):
	x = np.append(x,i)
	X = np.random.randn(i,i)
	Y = np.random.randn(i,i)
	ans1 = np.zeros((i,i))
	ans2 = np.zeros((i,i))

	start=time.time()
	for i in range(X.shape[0]):
		for j in range(Y.shape[1]):
			ans1[i,j] = sum([x_data*y_data for x_data,y_data in zip(X[i,:],Y[:,j])])
	y1 = np.append(y1,time.time()-start)
	print("time = ",time.time()-start)

	start=time.time()
	ans2 = np.dot(X,Y)
	y2 = np.append(y2,time.time()-start)
	print("time = ",time.time()-start,"\n")


plt.plot(x,y1,"-o",label="without numpy.dot")
plt.plot(x,y2,"-^",label="use numpy.dot")

plt.title("Time[s] - Matrix_size")
plt.xlabel("Matrix_size")
plt.ylabel("Time[s]")
plt.legend(loc='upper left')
plt.grid(True)

plt.savefig('mondai1.png')
plt.show()
plt.close()