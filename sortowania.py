tab=[4,7,21,2,1,1,6,67,10,8,7]

## sortowanie bąbelkowe
def sortowanie_babelkowe(tablica):
    for i in range(len(tablica)):
        for l in range(1,len(tablica)-i):
            if tablica[l-1]>tablica[l]:
                temp=tablica[l]
                tablica[l]=tablica[l-1]
                tablica[l-1]=temp

    return tablica
# print(sortowanie_babelkowe(tab))

## sortowanie przez wybór

def sortowanie_wybor(tablica):
    for  i in range(len(tablica)-1):
        min_index=i
        for l in range(i+1,len(tablica)):
            if tablica[l]<tablica[min_index]:
                min_index=l
        temp = tablica[i]
        tablica[i]=tablica[min_index]
        tablica[min_index]=temp
    return tablica
# print(sortowanie_wybor(tab))

## sortowanie przez wstawianie

def sortowanie_wstawianie(tablica):
    for i in range(1,len(tablica)):
        temp=tablica[i]
        j=i-1
        while j>=0 and tablica[j]>temp:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=temp
    return tablica
print(sortowanie_wstawianie(tab))