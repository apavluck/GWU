
def homework3(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print homework3(4)

# FUNCTIONS RETURN A VALUE
# SUBROUTINES DO CALCUALTIONS

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


def isfib(x,z):
    k = fib(10)
    print k
    for items in k:
        if items == z:
            print items, z
            q = True
            break
        else:
            print items, z
            q = False
    return q

#q = fib(10)
#print q
#print q[4]

print isfib(10,89)



def is_prime(n):
    for i in range(3,n):
        if n % i == 0:
            return False
        print n, i, n / i
    return True

print is_prime(2999)