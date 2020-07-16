# First line
a = ' '
print(a, 'X', a, '|', sep='', end='')
for i in range(2, 10):
    print('   ', i, sep="", end='')
print()


# Second line
print('---+', sep='', end='')
b = '----'
for i in range(2, 10):
    print(b, sep='', end='')
print()


# Third line
for i in range(2, 10):
    print(' ', i, ' ', '|', sep='', end='')
    for j in range(2, 10):
        if (i*j<10):
            print('   ', i * j, sep='', end='')
        else:
            print('  ', i * j, sep='', end='')
    print()
