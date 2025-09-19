def f(x, a, b, c): 
    return a*(x**2)+b*x + c

def minimize(f, range_, n=1000):
    a = min(range_)
    b = max(range_)
    delta_x = (b-a) / n 
    
    min_ = 100000000000
    minimizer_ = a
    for i in range(n): 
        xi = a + delta_x*i 
        if f(xi) < min_: 
            min_ = f(xi)
            minimizer_ = xi

    return minimizer_, min_

h = lambda x: f(x, 1, 1, 1)
minimize(h, [-10, 10], n=100)