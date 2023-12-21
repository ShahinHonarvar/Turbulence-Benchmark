
import re

def all_left_right_truncatable_prime(n):
    return sorted(set(re.findall(r'(2[1-9]99|99[1-9]99|99[1-9][0-9][0-9]99|9[1-9][0-9][0-9][0-9]99|[1-9][0-9][0-9][0-9]99)', str(n[23]))))
