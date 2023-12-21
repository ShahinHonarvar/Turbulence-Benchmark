
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[87]
    result = []
    for i in range(2, x):
        if is_prime(i):
            curr_num = str(i)
            while len(curr_num) > 1:
                curr_num = curr_num[:-1]
                if not is_prime(int(curr_num)):
                    break
            else:
                result.append(i)
    return result
