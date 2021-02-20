def f0(x,coef):
    return coef[0]* x**2 + coef[1]*x + coef[2]


def f1(x, coef):
    return coef[0]*x**4 + coef[1]*x**3 + coef[2]*x**2 + coef[3]*x + coef[4]


def fib(n):
    if n in [0,1]:
        return 1
    return fib(n - 1) + fib(n - 2)
  
def fib_search(f, bounds, tol, coef, max_eps = 0.01):
    F = (1 + 2 * max_eps) / (tol/(bounds[1] - bounds[0]))
    N = 1
    while fib(N+1) < F:
        N+=1
    for k in range(N):

        p = 1 - fib(N-k) / fib(N-k+1)
        if p == 1/2:
          p -= max_eps / 2

        lmbd = bounds[0] + p * (bounds[1] - bounds[0])
        nu = bounds[0] +(1 - p) * (bounds[1] - bounds[0])
        if f(lmbd, coef) < f(nu, coef):
            bounds[1] = nu
        else:
            bounds[0] = lmbd

    return (bounds[1] + bounds[0]) / 2
    



type = int(input())
f = f0 if (type == 0) else f1
coef = [i for i in map(float,input().split())]
bounds = [0, 0]
bounds[0], bounds[1], tol = map(float, input().split())
r1 = fib_search(f, bounds, tol, coef)
print("{:.10f}".format(r1))



###В данной задаче Вам необходимо реализовать метод Фибоначчи для функций двух типов:
f0(x) = c0x2+c1x+c2
f1(x) = c0x4+c1x3+c2x2+c3x+c4
В качестве параметра  для последнего шага возьмите значение  = 0.01. На последнем шаге Вы должны отнять  от p = 0.5 и сделать последнюю итерацию алгоритма.###

