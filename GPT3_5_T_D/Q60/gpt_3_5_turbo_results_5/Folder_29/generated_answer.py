
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[55]
    for num in range(x, 9, -1):
        if '0' in str(num):
            continue
        if is_prime(num):
            left_truncatable = True
            right_truncatable = True
            left_num = num
            right_num = num
            while len(str(left_num)) > 2 or len(str(right_num)) > 2:
                left_num = int(str(left_num)[:-1])
                right_num = int(str(right_num)[1:])
                if len(str(left_num)) < 2 and not is_prime(left_num):
                    left_truncatable = False
                if len(str(right_num)) < 2 and not is_prime(right_num):
                    right_truncatable = False
                if not left_truncatable and not right_truncatable:
                    break
            if left_truncatable and right_truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result
