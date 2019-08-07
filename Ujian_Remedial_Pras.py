# No.1

def find_short(s):
    length=[]
    x = s.split()
    for item in x:
        length.append(len(item))
    length.sort()
    return print(length[0])

find_short("Many people get up early in the morning")
find_short("Every office would getting newest monitor")
find_short("Create new file after this morning")

# No.2
def persistence(x):
    angka = x
    step = 0
    while (angka>=10):
        z = angka
        y = str(z)
        angka1 = 1
        for i in range (len(y)):
            angka1 *= int(y[i])
        step += 1
        angka = angka1
    return print(step)

persistence(39)
persistence(999)
persistence(4)

# No.3
def multiplication_table(row,col):
    list1=[1,2,3]
    z=''
    for item2 in range(row):
        for item3 in range(col):
            if item2 > item3:
                z+='{}'.format(list1[item3]*(item2+1))
            else:
                z+='{}'.format(list1[item2]*(item3+1))
        z+='\n'
    print(z)

multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)

# No.4

def alphabet_position(text):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,}
    a = text.split()
    z = ''
    for x in a:
        for letter in x.lower():
            if letter in alphabet:
                z += str(alphabet[letter])
                z += ' '
            else:
                pass
    return z

print(alphabet_position("The sunset sets at twelve o'clock"))    
print(alphabet_position("it's never too late to try"))
print(alphabet_position("Have you done your homework?"))

#No.5 (bonus)
def is_prime(num):
    num1 = 3
    lists = [2]
    while lists[-1] < num:
        for p in lists:
            if num1 % p == 0:
                break
        else:
            lists.append(num1)
        num1 += 2
    if lists[-1] == num:
        return True
    else:
        return False

print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))   
print(is_prime(5099))