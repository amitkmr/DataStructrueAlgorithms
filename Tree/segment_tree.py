"""
Given an array A of size N, there are two types of queries on this array.

: In this query you need to print the minimum in the sub-array .
: In this query you need to update .
Input:
First line of the test case contains two integers, N and Q, size of array A and number of queries.
Second line contains N space separated integers, elements of A.
Next Q lines contain one of the two queries.

Output:
For each type 1 query, print the minimum element in the sub-array .

Contraints:


"""


# build the segment tree/ Insert to node to segment tree

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def build_tree(tree, node, start, end, arr):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start+end)//2

    build_tree(tree,left(node),start,mid,arr)
    build_tree(tree,right(node),mid+1,end,arr)

    tree[node] = tree[left(node)] + tree[right(node)]

def query_tree(tree,node,start,end,l,r):
    if start > r or end < l:
        return 0

    if l <= start and end <= r:
        return tree[node]
    
    # when the interval is half this side and half that side

    mid = (start + end)//2

    return query_tree(tree,left(node),start, mid,l,r) + query_tree(tree,right(node),mid+1, end,l,r)


def update_tree(tree,node, start,end,idx,arr,val):
    if start == end:
        arr[idx]+=val
        tree[node]+=val
        return

    mid = (start+end)//2

    if idx < mid:
        update_tree(tree,left(node),start,mid,idx,arr,val)
    else:
        update_tree(tree,right(node),mid+1,end,idx,arr,val)
    
    tree[node] = tree[left(node)] + tree[right(node)]

def main():
    arr = [5,4,3,2,1]
    n = len(arr)
    tree = [0]*(2*n-1)

    build_tree(tree,0,0,n-1,arr)
    print(query_tree(tree,0,0,n-1,3,4))
    update_tree(tree,0,0,n-1,3,arr,6)
    print(query_tree(tree,0,0,n-1,3,4))

if __name__ == '__main__':
    main()
    