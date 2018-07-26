"""

Q. Why to learn another data structure when we have segment tree which can performed the same 
operation with same time complexity. 

Ans :  It’s because binary indexed trees require less space and are very easy to implement during programming contests (the total code is not more than 8-10 lines).

"""


def getSum(tree,i):
    g_sum = 0
    i+=1 # adjust the tree by one index
    while(i>0):
        g_sum+=tree[i]
        i-=i&(-i)
    return g_sum

def update(tree,n,i,val):
    i+=1 # adjust the tree by one index
    while(i<=n):
        tree[i]+=val
        i+= i&(-i)


def main():
    arr = [2,3,4,-5,6,2,7,8,1,23]
    tree = [0]*(len(arr)+1)
    i = 0
    while(i<len(arr)):
        update(tree,len(arr),i,arr[i])
        i+=1

    print(getSum(tree,9))

if __name__ == '__main__':
    main()
    