def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
	print("bisection method fails. f(a) and f(b) must have opposite signs.")
	return None
    iteration = 0
    while (b-a)/2 > tol and iteration < max_iter:
	c=(a+b)/2
	print(f"Iteration {iteration+1}:c={c:.6f},f(c)={f(c):.6f}")
	if f(c)==0:
	   return c
	elif f(a)*f(c)<0:
	    b=c
	else:
	    a=c
	iteration+=1
    return (a+b)/2
if __name__ =="__main__":
    f=lambda x: x**3 -x -2
    root=bisection(f, 1, 2)
    print(f"\nApproximate root:{root:.6f}")
