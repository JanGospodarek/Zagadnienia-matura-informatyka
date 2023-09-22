def horner(wspolczynniki,stopien,argument):
    wynik=wspolczynniki[0]
    for i in range(stopien):
        wynik=wynik*argument+wspolczynniki[i]
    return wynik
print(horner([3,2,1,3],3,2))