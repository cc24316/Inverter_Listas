print("programa para inverter lista")

def inversao (L):
    ret=[]
    for elemento in L:
        ret = [elemento]+ret
    return ret
    
    
print(inversao([5,4,3,2,56]))
