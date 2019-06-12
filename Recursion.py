def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1) #


def fact(a):
    if a ==1:
        return a
    else:
        return a * fact(a-1)


def iterPower(base, exp):
    result = 1
    while exp >= 1:
        result *= base
        exp -= 1
    return result


def recurPower(base, power):
    """ base ^ 0 = 1 amd base^ 1 = base. these are constants """
    if power == 1:
        return base
    else:
        return base * recurPower(base, power-1)
# we are breaking down the problem here to the base case

def gcdIter(first, second):
    """ test == smaller of the two
    iteratively reduce by 1 until test divides both a and b without remainder """
    test = first if first < second else second
    while test >=1:
        if first % test==0 and second % test == 0:
            return test
        else:
            test-=1
    return 1
    

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)


def toChars(s):
    s = s.lower()
    word = ''
    # alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in s:    
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            word+=letter
    return word


def isPal(s):
    charword = toChars(s)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

s = 'aba aba'
print(isPal(s))
print(gcdRecur(10, 67))
