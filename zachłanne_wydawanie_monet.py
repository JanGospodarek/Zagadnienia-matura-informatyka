monety=[1,2,5]
def wydawanie(reszta):
    monety_do_wydania=[]
    while reszta>0:
        nominal_monety=0
        for liczba in monety:
            if liczba<=reszta and liczba>nominal_monety:
                nominal_monety=liczba
        monety_do_wydania.append(nominal_monety)
        reszta=reszta-nominal_monety
    return monety_do_wydania

print(wydawanie(87))