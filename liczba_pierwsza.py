#Sprawdz czy podana liczba jest liczbą pierwszą
def czy_pierwsza(n):
    pierwsza=True
    if n<2:
        pierwsza=False
    for i in range(2,n):
        if n%i==0:
            pierwsza=False
    return pierwsza

print(czy_pierwsza(31))