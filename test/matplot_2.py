import matplotlib.pyplot as plt
import numpy as np
import time

x = np.arange(10.0)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x,y)
fig.canvas.draw()

fig.show()
fig.canvas.flush_events()

num_plot = 0

while 1:
	x += 0.1 
	y = np.sin(x)
	line.set_xdata(x)
	line.set_ydata(y)
	ax.set_xlim([x.min(),x.max()])
	fig.canvas.draw()
	fig.canvas.flush_events() # <-これがないと画面に描画されない。
	for i in range(10000):
		print(i)

