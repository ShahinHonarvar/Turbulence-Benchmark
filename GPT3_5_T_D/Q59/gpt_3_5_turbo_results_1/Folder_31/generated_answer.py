
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    result = []
    for num in range(x-1, 0, -1):
        num_str = str(num)
        if '0' not in num_str:
            is_truncatable_prime = True
            for i in range(len(num_str)):
                trunc_num = int(num_str[i:])
                if not is_prime(trunc_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return result
