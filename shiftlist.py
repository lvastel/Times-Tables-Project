
y = []
for i in range(10):
    y.append(i)
print(y)

def shift_right(y):
    try:
        return y[1:] + [y[0]]
    except IndexError:
        return y

print(shift_right(y))

a = shift_right(y)

for i in a:
    y.append(i)

print(y)