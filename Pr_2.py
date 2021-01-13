with open('numere.txt', 'r') as f:
    a=f.readline()
    b=f.readline()
with open('produs.txt', 'w') as f:
    if int(a)<int(b):
        x=int(a)*3
        y=int(b)*2
        f.write(str(x))
        f.write('\n')
        f.write(str(y))
    if int(a)>int(b):
        x=int(a)*2
        y=int(b)*3
        f.write(str(x))
        f.write('\n')
        f.write(str(y))