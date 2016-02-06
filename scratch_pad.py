#fibonacci
def fib (x):
    a = 0
    b = 1
    f = [1,1]
    while a < x:
        q = f[a] + f[b]
        f.append(q)
        a += 1
        b += 1
    return f


k = fib(10)
print k
z = 55


for items in k:
    if items == z:
        print items, z
        j = True
        break
    else:
        print items, z
        j = False
print j