def arraySum(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 0:
        return 0
    return arr[n-1] + arraySum(arr, n-1)