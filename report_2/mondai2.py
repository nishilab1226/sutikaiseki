# -*- utf-8 -*-
from sympy import sin,cos,symbols,diff,pi
import matplotlib.pyplot as plt
#変数の宣言
x,y = symbols("x y")

#関数
funcs = [x**3-3*x**2+9*x-8,
		sin(x),
		cos(x),
		sin(x/4)-cos(x/4)]
#誤差
e = 1e-5

#値保持リスト
route_val_dichotomy = []
route_val_newton = []
tmp_arr = []

#2分法
def dichotomy(f,xn,xp,e):
	xc = (xn+xp)/2
	tmp_arr.append(xc)
	if abs(f.subs(x,xc)) < e: return xc
	d = dichotomy
	return d(f,xn,xc,e) if f.subs(x,xc) > 0 else d(f,xc,xp,e)

#ニュートン法
def newton(f,a,e):
	b = a - f.subs(x,a)/diff(f,x).subs(x,a)
	tmp_arr.append(b)
	if abs(b-a) < e:
		return b
	return newton(f,b,e)

#グラフ表示
def show_graph(arr,name):
	plt.plot(arr[0],marker="o",label="x^3+3x^2+9x-8")
	plt.plot(arr[1],marker="^",label="sin(x)")
	plt.plot(arr[2],marker="*",label="cos(x)")
	plt.plot(arr[3],marker="D",label="sin(x/4)-cos(x/4)")

	plt.title("route_val - The number of iterations")
	plt.xlabel("The number of iterations")
	plt.ylabel("route_val")
	plt.legend(loc='upper right')
	plt.grid(True)
	plt.savefig(name+".png")
	plt.show()
	plt.close()

#main関数
if __name__ == "__main__":
	#二分法
	print("start dichotomy...")
	xnp = [[-7.5,7.5],
			[-1.0,1.5],
			[3.0,0.0],
			[0.0,5.0]]
	for i in range(len(funcs)):
		ans = dichotomy(funcs[i],xnp[i][0],xnp[i][1],e)
		route_val_dichotomy.append(tmp_arr)
		tmp_arr = []
	show_graph(route_val_dichotomy,"mondai2_dichotomy")
	print("...end dichotomy"+"\n")

	#ニュートン法
	print("start newton...")
	a = [-7.5,-1.0,2.5,5.0]
	for i in range(len(funcs)):
		ans = newton(funcs[i],a[i],e)
		route_val_newton.append(tmp_arr)
		tmp_arr = []
	show_graph(route_val_newton,"mondai2_newton")
	print("...end newton")

