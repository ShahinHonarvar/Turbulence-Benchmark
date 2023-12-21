
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    result = []

    for n in range(2, x):
        if '0' in str(n):
            continue
        is_left_truncatable_prime = True
        temp = str(n)
        while len(temp) > 1:
            temp = temp[1:]
            if not is_prime(int(temp)):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            result.append(n)

    result.sort()
    return result
