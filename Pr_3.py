with open('globulet.txt', 'r') as f:
    a=f.readline()
with open('bradut.txt', 'w') as f:
    total=int(a)+(int(a)+3)+(int(a)+(int(a)+3)-2)
    f.write(str(total))