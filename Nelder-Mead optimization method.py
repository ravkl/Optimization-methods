import numpy as np

def f0(x,coef):
    return 4*(x[0] - coef[0])**2 + (x[1] - coef[1])**2
def f1(x,coef):
    return (x[0]-coef[0])**2 + x[0]*x[1] + coef[1]*(x[1]-3)**2

def Nealder_Mead(f, x0, tol, coef):
    al = 1
    beta = 0.5
    gam = 2
    # Your Code
    sigma = tol + 1
    flag = False
    while sigma > tol:  
        b,g,w = sorted(x0, key=lambda x: f(x,coef))
        mid = (b + g) / 2
        sigma = np.sqrt(((f(b,coef) - f(mid,coef)) ** 2 + (f(g,coef) - f(mid,coef)) ** 2 + (f(w,coef) - f(mid,coef)) ** 2) / 2)

        #reflection
        xr = mid + al * (mid - w)
        if f(xr,coef) <= f(b,coef):
                # expansion
            xe = mid + gam * (xr - mid)
            if f(xe,coef) < f(b,coef):
                w = xe
            else:
                w = xr
        if f(b,coef) < f(xr,coef) and f(xr,coef) <= f(g, coef):
            w = xr
        flag = False
        if f(w,coef) >= f(xr,coef) and f(xr,coef) > f(g, coef):
            flag = True
            w = xr
        if f(xr,coef) > f(w,coef):
            flag = True
        if flag:
            xc = mid + beta * (w - mid)
            if f(xc,coef) < f(w,coef):
                w = xc
        if f(xr,coef) > f(g,coef):        
                # contraction
            xc = mid + beta * (w - mid)
            if f(xc,coef) < f(w,coef):
                w = xc

        # update points
        x0[0] = w
        x0[1] = g
        x0[2] = b
    return min(f(x0[0],coef), f(x0[1],coef), f(x0[2], coef))
    #шаманил еще итерацию не вышло(
    b,g,w = sorted(x0, key=lambda x: f(x,coef))
    mid = (b + g) / 2
    sigma = np.sqrt(((f(b,coef) - f(mid,coef)) ** 2 + (f(g,coef) - f(mid,coef)) ** 2 + (f(w,coef) - f(mid,coef)) ** 2) / 2)
    xr = mid + al * (mid - w)
        
    if f(xr,coef) < f(g,coef):
        w = xr
    else:
        if f(xr,coef) < f(w,coef):
            w = xr
        c = (w + mid)/2
        if f(c,coef) < f(w,coef):
            w = c
    if f(xr,coef) < f(b,coef):
            # expansion
        xe = mid + gam * (xr - mid)
        if f(xe,coef) < f(xr,coef):
            w = xe
        else:
            w = xr
    if f(xr,coef) > f(g,coef):        
            # contraction
        xc = mid + beta * (w - mid)
        if f(xc,coef) < f(w,coef):
            w = xc
    x0[0] = w
    x0[1] = g
    x0[2] = b



type = int(input())
f = f0 if (type == 0) else f1
coef = [i for i in map(float,input().split())]
x0 = []
for k in range(3):
    x0.append(np.array([i for i in map(float,input().split())]))
tol = float(input())
r1 = Nealder_Mead(f, x0, tol, coef)
print("{:.10f}".format(r1))
