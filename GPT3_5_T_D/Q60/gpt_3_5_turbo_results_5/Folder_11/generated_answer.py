
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[86]
    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        prime = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[:j+1])) or not is_prime(int(str(i)[j:])):
                prime = False
                break
        if prime:
            result.append(i)
    return sorted(result)
