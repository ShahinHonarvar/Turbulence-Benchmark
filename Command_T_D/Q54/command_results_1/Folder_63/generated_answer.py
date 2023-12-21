def all_right_truncatable_prime(test_list):
    res = []
    for num in test_list:
        if str(num) in list(str(num) for x in range(2, num) if x ** 2 <= num):
            res += [num]
    return res
