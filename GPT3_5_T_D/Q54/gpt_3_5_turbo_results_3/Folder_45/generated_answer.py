
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    result = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            for j in range(len(str(i)) - 1):
                trunc = int(str(i)[:-j-1])
                if not is_prime(trunc):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result)
