
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for i in range(2, x):
        prime = True
        num = str(i)
        if '0' in num:
            continue
        while num:
            if not is_prime(int(num)):
                prime = False
                break
            num = num[1:]
        if prime:
            result.append(i)
    return sorted(result, reverse=True)
