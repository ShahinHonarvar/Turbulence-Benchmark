
def all_left_right_truncatable_prime(test_list):
    res = []
    for num in test_list:
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res


def is_left_right_truncatable_prime(num):
    prime_list = []
    for i in range(2, int(str(num)[0]) + 1):
        if num % i == 0:
            break
        elif num % i == 1:
            prime_list.append(i)
        elif num % i == 5:
            prime_list.append(i)
            prime_list.append(5)
    return num not in prime_list
