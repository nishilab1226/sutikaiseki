def dichotomy(xn,xp):
	xc = (xn+xp)/2
	if abs(f(xc)) < 1.0e-6: return xc
	d = dichotomy
	return d(xn,xc) if f(xc) > 0 else d(xc,xp)

f = lambda x:x**2-2
xp = 2
xn = 1
print(f"xp = {xp} , xn = {xn} , f(xp)*f(xn) = {f(xp)*f(xn)}")
print("ans = ",dichotomy(xn,xp))