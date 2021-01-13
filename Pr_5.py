with open('numar.txt', 'r') as f:
    n=f.readline()

    n1=int(n)*1
    n2=int(n)*2
    n3=int(n)*3
    n4=int(n)*4
    n5=int(n)*5
    n6=int(n)*6
    n7=int(n)*7
    n8=int(n)*8
    n9=int(n)*9
    n10=int(n)*10

with open('inmultire.txt', 'w') as f:

    f.write('1*'+n+'='+str(n1))
    f.write('\n')
    
    f.write('2*'+n+'='+str(n2))
    f.write('\n')

    f.write('3*'+n+'='+str(n3))
    f.write('\n')

    f.write('4*'+n+'='+str(n4))
    f.write('\n')

    f.write('5*'+n+'='+str(n5))
    f.write('\n')

    f.write('6*'+n+'='+str(n6))
    f.write('\n')

    f.write('7*'+n+'='+str(n7))
    f.write('\n')

    f.write('8*'+n+'='+str(n8))
    f.write('\n')

    f.write('9*'+n+'='+str(n9))
    f.write('\n')

    f.write('10*'+n+'='+str(n10))
    f.write('\n')