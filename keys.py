import random
def desc(n):
    a="0"
    if n<10:
        a=chr(48+n)
    else:
        a=chr(55+n)
    return a    
def pacs(n):
    a=0
    a=random.randrange(36) 
    return desc(a)

def packget(p):
    a=""
    for aa in range(p):
        a=a+str(pacs(16))
    return a 

print("\033c\033[43;30m\n")

for n in range(16):
    print(packget(16))
