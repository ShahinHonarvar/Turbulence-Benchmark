
def if_perfect_num(arr):
    index_10_number = arr[10]
    factors = []
    for i in range(1, index_10_number):
        if index_10_number % i == 0:
            factors.append(i)
    if sum(factors) == index_10_number:
        return True
    else:
        return False
