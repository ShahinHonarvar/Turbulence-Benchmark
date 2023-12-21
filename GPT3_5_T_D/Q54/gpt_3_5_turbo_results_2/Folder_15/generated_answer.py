
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[6]
    result = []
    for num in range(x-1, 0, -1):
        digits = str(num)
        prime = True
        for i in range(len(digits)):
            trunc = int(digits[:i+1])
            if not is_prime(trunc):
                prime = False
        if prime:
            result.append(num)
    return sorted(result, reverse=True)
