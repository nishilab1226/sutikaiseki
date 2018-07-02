from math import *
a = c = 1
b = 1.0e5

x1_b = lambda a,b,c:(-b+sqrt(b**2-a*c))/a
x2_b = lambda a,b,c:(-b-sqrt(b**2-a*c))/a

x1_a = lambda a,b,c:-c/(b+sqrt(b**2-a*c))
x2_a = lambda a,b,c:c/(-b+sqrt(b**2-a*c))

print("\nb>0 : ")
print(f"before_ans = ( x1 = {x1_b(a,b,c)} , x2 = {x2_b(a,b,c)} )")
print(f"after_ans = ( x1 = {x1_a(a,b,c)} , x2 = {x2_b(a,b,c)} )")
print("-"*80)
print("b<0 : ")
print(f"before_ans = ( x1 = {x1_b(a,-b,c)} , x2 = {x2_b(a,-b,c)} )")
print(f"after_ans = ( x1 = {x1_b(a,-b,c)} , x2 = {x2_a(a,-b,c)} )")