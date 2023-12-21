
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[25]
    for i in range(2, x+1):
        if is_prime(i):
            str_i = str(i)
            if '0' in str_i:
                continue
            is_truncatable = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
