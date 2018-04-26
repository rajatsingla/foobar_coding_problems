# def x(n,i,c):
#     if n<=0:
#         return c+1
#     else:
#         for j in range(i,n+1):
#             c=x(n-j,j+1,c)
#     return c        

# def answer(n):
#     return x(n,1,0)-1


# import operator as op
# def ncr(n, r):
#     r = min(r, n-r)
#     if r == 0: return 1
#     numer = reduce(op.mul, xrange(n, n-r, -1))
#     denom = reduce(op.mul, xrange(1, r+1))
#     return numer//denom

# print ncr(55,10)


def is_possible(x,y):
    tmp=0
    for i in range(x-1,-1,-1):
        if tmp>=y:
            return True
        tmp+=i
    return False

def get_count(n,s,tmp):
    count=0
    if tmp.get(str(n)+'_'+str(s)):
        return tmp.get(str(n)+'_'+str(s))
    for i in range(n-s,1,-1):
        if i > n-i:
            count+=1
            if tmp.get(n-i):
                count+=tmp.get(n-i)
        else:
            if is_possible(i,n-i):
                res=get_count(n-i,n-2*i+1,tmp)
                if res:
                    count+=res
    tmp[str(n)+'_'+str(s)]=count
    return count

def answer(n):
    tmp={}
    for i in range(3,n+1):
        tmp[i]=get_count(i,1,tmp)
    return tmp


print answer(10)