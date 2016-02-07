'''

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

'''

def breakitintoletters(name):
    for char in name:
        print char


word = "Mississippi"
count = 0

for letter in word:
    if letter == "s":
        count +=1

print count


sentence = "This is a test program to see if I have the skills needed to do this!"

key = "program"
word = "is"

if word < key:
    print "your word is before program"
elif word > key:
    print "your word is after program"