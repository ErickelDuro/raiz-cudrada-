def raiz(a):
    x = 0
    while (x*x) <= a: x += 1
    if abs(a - (x*x)) > abs(a - ((x-1)*(x-1))): x -= 1
    return round((a + (x*x))/(2*x), 4)

print(raiz(int(input("Ingresar el valor >>> "))))

