def binary(x):
    converted=0
    negyzet=0
    while x>0:
        converted+=2**negyzet*(x%10)
        x//=10
        negyzet+=1
    return converted

n=int(input("Hany szamot ellenorizzek: "))
lst=[]
lstFinal=[]
for i in range(n):
    a=int(input("Adjon meg 5 számjegyű bináris számokat: "))
    lst.append(a)


for i in range(n):
    x=binary(lst[i])
    if x%3==0:
        tuple=lst[i],x
        lstFinal.append(tuple)

print(lstFinal)
