z = int(input('number'))

y = []
for i in range(10):
    y.append(i)
print(y)

def shift_left(y):
    try:
        return y[1:] + [y[0]]
    except IndexError:
        return y

e = y
print(e)
for i in range(z):
    e = shift_left(e)
    print(e)
    ##adding shifted list to base list
    for i in e:
        y.append(i)
print(y)
