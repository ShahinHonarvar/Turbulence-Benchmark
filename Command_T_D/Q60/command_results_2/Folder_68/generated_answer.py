
import re

def all_left_right_truncatable_prime(test_list):
    return sorted(set(list(map(str, list(range(2, test_list[0] + 1)))), key=lambda x: str(x)), reverse=True)
