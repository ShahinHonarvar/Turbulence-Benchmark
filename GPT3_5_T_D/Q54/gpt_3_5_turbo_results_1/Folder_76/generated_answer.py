
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[370]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp = str(num)
            is_right_truncatable = True
            while is_right_truncatable and len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    is_right_truncatable = False
            if is_right_truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result
