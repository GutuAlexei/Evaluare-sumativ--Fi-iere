with open('c:/Users/user/Desktop/INPUT.txt', 'rt')as f: 
    linii=list(f) 
print('NR. Nume   Prenume nota1 nota2 nota3  ') 
for linie in linii: 
    campuri=linie.split()
    print(linie)
with open("Rezerva.txt", "w") as f:
    f.write('NR. '+'Nume   '+'Prenume '+'nota1 '+'nota2 '+'nota3 '+'\n')
    for b in linii:
        f.write(str(b)+"\n")
with open("Output.txt", "w") as f:
    for i in linii:
        nota=i.split()
        x=nota[0]+' '+nota[1]+' '+nota[2]
        media=str(float(nota[3])+float(nota[4])+float(nota[5])/3)
        final=x+' '+media+'\n'
        with open('OUTPUT.txt','a') as f:
            f.write(final)
with open('OUTPUT.txt','r') as f:
    list3=f.readlines()


