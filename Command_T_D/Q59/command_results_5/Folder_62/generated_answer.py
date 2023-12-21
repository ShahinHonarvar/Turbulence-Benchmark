import re
def all_left_truncatable_prime(arr):
    # function to return all left-truncatable prime numbers less than x
    # arr[70] is passed as x
    return sorted(set(re.findall(r'[1-9][0-9]*', str(arr[70]))))
