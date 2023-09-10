# ciąg fibonacciego o danej ilosci wyrazów

def iter(n):
    a=0
    b=1
    liczby=[]
    for i in range(0,n):
        liczby.append(b)
        b+=a
        a=b-a
    return liczby
print(iter(100))

# rekurencyjnie- n-ty wyraz ciagu fibonacciego
def rekur(n):
    if n<3:
        return 1
    return rekur(n-2)+rekur(n-1)

print(rekur(10))