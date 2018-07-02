import numpy as np
import matplotlib.pyplot as plt

xmin,xmax = -np.pi , np.pi
x = np.arange(xmin,xmax,0.1)
cos = np.cos(x)
sin = np.sin(x)
tan = np.tan(x)

plt.plot(x,cos,label="cos")
plt.plot(x,sin,label="sin")
plt.plot(x,tan,label="tan")

plt.title("sin(x) and cos(x) and tan(x)")
plt.grid(True)
plt.xlim(xmin,xmax)
plt.ylim(-1,1)
plt.legend(loc="upper left")

plt.show()