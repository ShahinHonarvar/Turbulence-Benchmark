
def if_perfect_num(arr):
    num = arr[60]
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num if num > 1 else False
