
def if_perfect_num(arr):
    if len(arr) < 4:
        return False
    num = arr[3]
    sum_divisors = sum([i for i in range(1, num // 2 + 1) if num % i == 0])
    return sum_divisors == num - 1
