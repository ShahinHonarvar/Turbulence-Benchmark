import sys
def all_left_truncatable_prime(test_case):
    x = int(test_case[24])
    return sorted(list(set(test_case[:24]) + test_case[25:]))
