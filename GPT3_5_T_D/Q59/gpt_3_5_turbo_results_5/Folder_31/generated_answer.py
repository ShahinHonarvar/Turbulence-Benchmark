
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    results = []
    for i in range(x, 10, -1):
        num = str(i)
        if '0' not in num:
            is_left_truncatable = True
            for j in range(len(num)-1):
                truncated_num = int(num[j+1:])
                if not is_prime(truncated_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                results.append(i)
    return results
