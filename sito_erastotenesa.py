import math

def sito(n):
    liczby =[True]*(n+1)
    for i in range(2,int(math.ceil(math.sqrt(n)))):
        if liczby[i]:
            for k in range(i*i,n+1,i):
                liczby[k]=False
    return liczby
print(sito(25)) #indeks 0 i 1 to nie liczby pierwsze !!!!!!!!!!!!! LOOPUJEMY FOREM W RANGE(2,N+1)
