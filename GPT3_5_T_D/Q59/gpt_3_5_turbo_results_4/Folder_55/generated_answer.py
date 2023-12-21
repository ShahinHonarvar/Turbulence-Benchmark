
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for i in range(x-1, 0, -1):
        num = str(i)
        if '0' in num:
            continue
        is_lt_prime = True
        for j in range(len(num)):
            trunc_num = int(num[j:])
            if not is_prime(trunc_num):
                is_lt_prime = False
                break
        if is_lt_prime:
            result.append(i)
    return result
