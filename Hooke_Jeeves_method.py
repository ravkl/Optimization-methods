import numpy as np

def f0(x,coef):
    return coef[0]*x[0]**4 + coef[1]*x[1]**3 + coef[2]*x[1]**2 + coef[3]*x[0] + coef[4]
def f1(x,coef):
    return x[0]**2 + coef[0]*x[0]*x[1] + coef[1]*(x[1]-3)**2

def Hooke_Jeeves(f, x0, tol, coef):
    delta = np.array([1.0, 1.0])
    al = 2
    lam = 1
    #x = copy(x0)

    while all(delta) > tol:
        xl = x0 - delta * [1.0, 0.0]
        xr = x0 + delta * [1.0, 0.0]
        #x1 check
        if f(x0, coef) <= f(xl, coef) and f(x0,coef) <= f(xr, coef):
            delta[0] /=  al
        elif f(xl, coef) < f(xr, coef):
            x0[0] = xl[0]
        else:
            x0[0] = xr[0] 
        #x2 check
        xd = x0 - delta * [0.0, 1.0]
        xu = x0 + delta * [0.0, 1.0]
        if f(x0, coef) <= f(xd, coef) and f(x0,coef) <= f(xu, coef):
            delta[1] /=  al
        elif f(xu, coef) < f(xd, coef):
            x0[1] = xu[1]
        else:
            x0[1] = xd[1]
    return x0
type = int(input())
f = f0 if (type == 0) else f1
coef = [i for i in map(float,input().split())]
x0 = np.array([i for i in map(float,input().split())])
tol = float(input())
r1 = Hooke_Jeeves(f, x0, tol, coef)
print("{:.10f} {:.10f}".format(r1[0], r1[1]))
