import numpy as np
import time
import matplotlib.pyplot as plt


x = [0]
y = [0]

fig, ax = plt.subplots()
line, = ax.plot(x,y)
ax.set_xlim([min(x),max(x)])
ax.set_xlim([min(y),max(y)])
fig.show()
fig.canvas.draw()
fig.canvas.flush_events()

for i in range(100,401,100):
	start=time.time()
	X = np.random.randn(i,i)
	Y = np.random.randn(i,i)

	x.append(i)
	y.append(time.time()-start)
	line.set_xdata(x)
	line.set_ydata(y)
	ax.set_xlim([min(x),max(x)*1.1])
	ax.set_ylim([min(y),max(y)*1.1])
	fig.canvas.draw()
	fig.canvas.flush_events()

print("X = ",X)
print("Y = ",Y,"\n")

start=time.time()
ans = np.dot(X,Y)
print("np.dot(X,Y) >>> ",ans)
print("time = ",time.time()-start,"\n")


start=time.time()
for i in range(X.shape[0]):
	for j in range(Y.shape[1]):
		ans[i,j] = np.sum(X[i,:]*Y[:,j])
print("for(X,Y) >>> ",ans)
print("time = ",time.time()-start)
