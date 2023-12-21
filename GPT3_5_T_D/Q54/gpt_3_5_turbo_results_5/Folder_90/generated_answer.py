
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    result = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            num = str(i)
            is_truncatable_prime = True
            for j in range(1, len(num)):
                truncated_num = int(num[:-j])
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(i)
    result.sort(reverse=True)
    return result
