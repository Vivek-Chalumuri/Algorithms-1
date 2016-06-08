def mergesort(arr):
	
	n = len(arr)
	m = n/2
		
	if n > 1:
        
		a = mergesort(arr[:m])
		b = mergesort(arr[m:])

		i = 0
		j = 0
		k = 0
		
		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				arr[k] = a[i]
				i = i+1
			else:
				arr[k] = b[j]
				j = j+1
			k = k+1
		
		if i == len(a):
			return arr[:k] + b[j:]
		if j == len(b):
			return arr[:k] + a[i:]
		
	return arr