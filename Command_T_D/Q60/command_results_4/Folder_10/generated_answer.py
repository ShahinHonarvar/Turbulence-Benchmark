
import re

def all_left_right_truncatable_prime(n):
    numbers = re.findall(r'(2[13579])0*(99|91)', str(n))
    return sorted(set(numbers))
