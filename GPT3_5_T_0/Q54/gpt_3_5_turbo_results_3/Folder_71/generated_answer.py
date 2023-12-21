
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    result = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            num = str(i)
            is_truncatable = True
            for j in range(len(num)-1, 0, -1):
                if not is_prime(int(num[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
