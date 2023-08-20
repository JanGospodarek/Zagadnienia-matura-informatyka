# Wypisz czynniki pierwsze podanej liczby
def rozloz(n):
    czynniki = []
    k = 2
    while n >=2:
        while n % k == 0:
            n=n/k
            czynniki.append(k)
        k += 1
    return czynniki
print(rozloz(27))
