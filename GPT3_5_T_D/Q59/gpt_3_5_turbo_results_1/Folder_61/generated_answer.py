
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            is_left_truncatable = True
            s = str(i)
            while len(s) > 1:
                s = s[1:]
                if not is_prime(int(s)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
