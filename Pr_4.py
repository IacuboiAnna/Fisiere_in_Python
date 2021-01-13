with open('input.txt', 'r') as f:
    nr=f.readline()
with open('output.txt', 'w') as f:
    nr1=int(nr)-2
    nr2=int(nr)-1
    nr3=int(nr)+1
    nr4=int(nr)+2
    f.write(str(nr1))
    f.write(' ')
    f.write(str(nr2))
    f.write(' ')
    f.write(str(nr))
    f.write(' ')
    f.write(str(nr3))
    f.write(' ')
    f.write(str(nr4))