def partition(arr,p,r):
	pivot = arr[r]
	p = p - 1
	
	while(p<r):
		p = p + 1
		if arr[p] < pivot:
			continue
		j = p
		while(j<r):
			j = j + 1
			if arr[j] < pivot:
				break
		arr[p],arr[j] = arr[j],arr[p]
		if j == r:
			break

	return p 

def qsort(arr,p,r):
	if r < p:
		return
	q = partition(arr,p,r)
	qsort(arr,p,q-1)
	qsort(arr,q+1,r)

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int,input().split()))
		qsort(arr,0,n-1)
		print(arr)

if __name__ == '__main__':
	main()
