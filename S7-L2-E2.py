def é_hipotenusa(n):
    import math
    x = math.sqrt(n)
    if x == int(x):
        return True
    else:
        return False

n = int(input("n ="))
while n > 0:
    

print(é_hipotenusa(5))
print(é_hipotenusa(10))
print(é_hipotenusa(13))
print(é_hipotenusa(15))
print(é_hipotenusa(17))
print(é_hipotenusa(20))
print(é_hipotenusa(25))