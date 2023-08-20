# Wypisz dzielniki liczby n
def znajdz_dzielniki(n):
    dzielniki=[]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            dzielniki.append(i)
    return dzielniki

print(znajdz_dzielniki(56))