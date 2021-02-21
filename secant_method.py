def secant_search(f, df, x0, x1, coef, tol):
    fk = x1
    x1 = (df(x1,coef) * x0 - df(x0,coef) * x1) / (df(x1,coef) - df(x0,coef))
    x0 = fk
    while abs(x1 - x0) > tol:
        tmp = x1
        x1 = (df(x1,coef) * x0 - df(x0,coef) * x1) / (df(x1,coef) - df(x0,coef))
        x0 = tmp
    return x1


def f0(x,coef):
    return (coef[0]*x-1)**2+4*(4-coef[1]*x)**4

def df0(x,coef):
    return 2*coef[0]*(coef[0]*x-1)-16*coef[1]*(4-coef[1]*x)**3

def f1(x,coef):
    return coef[0]*(x - coef[1]) + (x - coef[2])**2

def df1(x,coef):
    return coef[0] - 2*coef[2] + 2*x


type = int(input())
f = f0 if (type == 0) else f1
df = df0 if (type == 0) else df1
coef = [i for i in map(float,input().split())]
x0, x1, tol = map(float, input().split())
r1 = secant_search(f, df, x0, x1,coef, tol)
print("{:.10f}".format(r1))
