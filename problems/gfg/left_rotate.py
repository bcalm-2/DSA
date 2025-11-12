def leftRotate(arr, d):
    # code here
  temp = arr[0:d]
  for i in range(d,len(arr)):
        arr[i-d] = arr[i]
  n = len(arr)
  arr[n-d:] = temp
  return arr