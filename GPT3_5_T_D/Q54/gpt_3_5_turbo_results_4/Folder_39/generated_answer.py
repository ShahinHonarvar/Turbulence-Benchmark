
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    result = []
    x = numbers[30]
    for i in range(x-1, 1, -1):
        if is_prime(i):
            is_right_truncatable = True
            num = str(i)
            for j in range(len(num)-1, 0, -1):
                if not is_prime(int(num[:j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
