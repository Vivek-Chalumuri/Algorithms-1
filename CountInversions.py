def merge_and_countINV(arr):
    n = len(arr)
    m = n/2
    count = 0
    
    if n > 1:
        
        a,c1 = merge_and_countINV(arr[:m])
        b,c2 = merge_and_countINV(arr[m:])
        
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
                count += len(a) - i
                
            k = k+1
            
        if i == len(a):
            return arr[:k] + b[j:], count + c1 + c2
        if j == len(b):
            return arr[:k] + a[i:], count + c1 + c2
        
    return arr, count      
