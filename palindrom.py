
def palindrom(slowo):
    czy_jest_palindromem=True
    for i in range(len(slowo)):
        if not slowo[i]==slowo[len(slowo)-1-i]:
            czy_jest_palindromem=False
    return czy_jest_palindromem
print(palindrom('bewsztyk'))