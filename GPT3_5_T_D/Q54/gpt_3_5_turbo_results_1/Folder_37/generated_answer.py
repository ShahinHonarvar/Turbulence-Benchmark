
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    result = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            temp = str(num)
            is_truncatable = True
            while temp != "":
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[:-1]
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
