# znalezienie NWD dwóch liczb

#iteracyjnie

def iter(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

print(iter(650,330))

#rekurencyjnie

def rekur(a,b):
    if(a!=b):
        if a>b:
          return rekur(a-b,b)
        else:
           return rekur(a,b-a)
    return a
print(rekur(650,330))

