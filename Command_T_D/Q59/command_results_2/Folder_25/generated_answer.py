import itertools
def all_left_truncatable_prime(test_tup):
    test_tup = tuple(test_tup)
    test_num = test_tup[92]
    test_num_str = str(test_num)
    test_left_str = test_num_str[0:10]
    test_left_str_list = list(test_left_str)
    test_left_str_iter = iter(test_left_str_list)
    test_left_str_list_prime = []
    test_left_str_list_non_prime = []
    for left_str in test_left_str_list:
        if left_str in test_left_str_list_prime:
            continue
        test_left_str_list_non_prime.append(left_str)
        test_left_str_list_prime.append(left_str)
        prime_str_list = []
        for i in range(1, len(left_str)):
            for prime_str in test_left_str_list_prime:
                new_str = left_str[0:i] + prime_str
                if new_str in test_left_str_list_prime:
                    continue
                elif all(new_str[i:].isprime() for i in range(1, len(left_str) - i)):
                    prime_str_list.append(new_str)
        test_left_str_list_prime += prime_str_list
    test_left_str_list_prime.sort()
    return test_left_str_list_prime
