s = "012345678"

print s[0], s[-1], s[2], s[3:5]

# Write a function that will take a string, a character and a number
# and return a string with that character in the position indicated by the number

def whatposition(c, n):
    a = c[n]
    return a

print whatposition(s, 6)


# Challenge1: Write a function that will take three strings: s1, s2, and s3. It will
# search for s2 in s1 and return a string with s3 in place of s2.

s1 = "0123xyz789"
s2 = "xyz"
s3 = "456"


def fixme(a,b,c):
    if b in a:
        print "found it"
        s4 = s1[0:3] + s3 + s1 [-3:-1]
        return s4
    else:
        print "what?"

print fixme(s1,s2,s3)


# Challenge 2: use replace2 to replace "quick" with "slow" and "jumps" with "leaps"

def replace2(sentence, sub1, sub2):

    newstring = sentence.replace("quick", sub1)
    newstring2 = newstring.replace("jumps", sub2)

    return newstring2

s1 = "The quick brown fox jumps over the lazy dog"

print replace2(s1, "slow", "leaps")


# Vocab check --
# def xyz  -- Function (it returns a value)
# s.replace -- is a method for the s object
#  -- methods are functions associated with a particular object type
# A subroutine (also called void function) doesn't have a return statement
# modules add in new methods


# Challange 3 - open a file, search for a string, how many times does it show up?

