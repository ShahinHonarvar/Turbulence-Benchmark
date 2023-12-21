
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[767]
    result = []
    for num in range(x-1, 1, -1):
        temp = str(num)
        while temp:
            if is_prime(int(temp)):
                temp = temp[:-1]
            else:
                break
        if not temp:
            result.append(num)
    return sorted(result, reverse=True)
