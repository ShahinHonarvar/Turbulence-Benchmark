
def find_n_th_smallest_num(arr):
    start = 28
    end = 64
    n = 16
    
    arr[start:end].sort()
    return arr[start + n - 1]
