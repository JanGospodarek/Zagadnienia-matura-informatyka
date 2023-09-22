
# sposob jest logiczny, można zrobić prościej i szybciej ale po co skoro to jest bardziej logiczne
def czy_anagram(slowo1,slowo2):
    litery1={}
    litery2={}
    for l in set(list(slowo1)):
        litery1[l]=slowo1.count(l)

    for l in set(list(slowo2)):
        litery2[l] = slowo2.count(l)

    for key in litery1:
        if not key in set(list(slowo2)):
            return False
        if not litery1[key]==litery2[key]:
            return False

    for key in litery2:
        if not key in set(list(slowo1)):
            return False
        if not litery1[key]==litery2[key]:
            return False
    return True

print(czy_anagram('adam','dama'))

