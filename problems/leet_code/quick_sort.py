def quickSort(arr, low, high):
    if low<high:
        partition_index=self.partition(arr,low,high)
        self.quickSort(arr,low,partition_index-1)
        self.quickSort(arr,partition_index+1,high)
def partition(arr, low, high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<high:
            i+=1
        while arr[j]>pivot and j>low:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j