# zamiana liczby z systemu dziesiętnego na dowolny system liczbowy o podstawie n, gdzie n należy do <2,16>, n e N

def zamien(liczba, podstawa):
    modula=[]
    while liczba>0 :
        print(liczba % podstawa)
        modula.append(str(liczba % podstawa))
        liczba=liczba//podstawa
    return  modula[::-1]


print(zamien(100,3))