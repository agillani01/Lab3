def max_101(x, y):
    if (x>y):
        return x
    return y

def max_of_three(x, y, z):
    float(x)
    float(y)
    float(z)
    if (x>=y and x>z):
        return x
    elif (y>x and y>=z):
        return y
    return z

def rental_late_fee(x):
    if (x<=0):
        return 0
    elif (x<=9):
        return 5
    elif (x<=15):
        return 7
    elif (x<=24):
        return 19
    else:
        return 100