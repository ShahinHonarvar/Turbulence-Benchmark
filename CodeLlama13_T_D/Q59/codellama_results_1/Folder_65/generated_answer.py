
def all_left_truncatable_prime(numbers):
    x = numbers[32]
    result = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and not any('0' in str(i) for i in range(2, int(str(i)[0])+1)):
            result.append(i)
    return sorted(result)
