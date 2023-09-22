
# bąbelkowe
dane=[1,5,6,2,3,1,1,78,21]
## latwo zapamiętać poniewaz wieksze bąbelki idą na koniec (porównujemy pary liczb)
# https://www.youtube.com/watch?v=4s44rXRdmhQ&ab_channel=kakaboc
# dla tablicy = [2,3,1,4]
# prownujemy pierwsza pare i nic nie zmieniamy (jest posortowana)
# porownujemy druga pare i otrzymujemy [2,1,3,4]
# ostatnia para jest juz posortowana
# jedziemy od poczatku
# porownujemy pierwsza pare i otrzymujemy [1,2,3,4]
# jedziemy do konca i okazuje sie ze wszystko juz jest posortowane
def sortowanie_babelkowe(tab):
    for i in range(len(tab)):
        for j in range(1,len(tab)):
            temp=tab[j]
            if tab[j-1]>tab[j]:
                tab[j]=tab[j-1]
                tab[j-1]=temp
    return tab
# print(sortowanie_babelkowe(dane))

# wybor
# https://www.youtube.com/watch?v=GUhWeJyHBCU&ab_channel=kakaboc
# znajdujemy minimum w ciagu i zamieniamy je z aktualnym elementem
# dla tablicy tab=[2,4,1,0]
# bierzemy pierwszy element i szukamy minimum w zbiorze [4,1,0]
# zamieniamy miejsce 2 z 0 [0,4,1,2]
# bierzemy drugi element 4 i zamieniamy z 1 [0,1,4,2]
# bierzemy znow 4 (trzeci element) i zamieniamy z 2 [0,1,2,4]

def sortowanie_wybor(tab):
    for i in range(0,len(tab)-1):
        min_index=i
        # znajdujemy minimum
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min_index]:
                min_index=j
        # zamieniamy miejscami z minimum
        temp= tab[i]
        tab[i]=tab[min_index]
        tab[min_index]=temp
    return tab
# print(sortowanie_wybor(dane))

# sortowanie przez wstawianie

# https://www.youtube.com/watch?v=8RkE7MbqVl8&ab_channel=kakaboc

def sortowanie_wstawianie(tab):
    for i in range(1,len(tab)):
        temp=tab[i]
        j=i-1
        while j>=0 and tab[j]>temp:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=temp
    return tab
# print(sortowanie_wstawianie(dane))

# scalanie

def sortowanie_scalanie(tab):

    return tab

print(sortowanie_scalanie(dane))
