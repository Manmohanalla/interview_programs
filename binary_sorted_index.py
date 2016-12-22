# array = [1, 5, 9, 23, 30] # sorted array of integers
# binary_search(array, val) -> index of val in array or -1 if val not in array
# binary_search(array, 9)->2
# recursive

def binary_search(array, val, l=0,h=None):
    if h == None:
        h= len(array)
    if len(array)!=0:
        mid =(l+h)/2
        value = array[mid]
        if value < val:
            l = mid+1
            return binary_search(array,val,l,h)
        elif value >val:
            h =mid
            return binary_search(array,val,l,h)
        elif value==val:
            return mid
        else:
            return -1
    else:
        return False
    
   

array = [1, 5, 9, 23, 30, 56, 78,79] 



print binary_search(array,78)
