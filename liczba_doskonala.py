#Sprawqdz czy liczba jest liczbą doskonałą

def czy_doskonala(n):
    dzielniki=[]
    suma=0

    for i in range(1,n):
        if n%i==0:
            dzielniki.append(i)
    for liczba in dzielniki:
        suma+=liczba
    if suma==n:
        return True
    else :
        return False
print(czy_doskonala(27))