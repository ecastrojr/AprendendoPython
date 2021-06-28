def maximo(x,y,z):
    if x > y and x > z:
        return x
    elif z > y and z > x:
        return z
    else:
        return y