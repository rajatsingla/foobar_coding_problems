# code for sorting elevator versions

def answer(l):
    for i in range(len(l)):
        tmp=map(int,l[i].split("."))
        l[i]=tmp
    
    l=sorted(l)
    
    for i in range(len(l)):
        tmp=map(str,l[i])
        tmp=".".join(tmp)
        l[i]=tmp
    return l



print answer(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])    