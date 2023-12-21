import re
def all_left_truncatable_prime(lims):
    return sorted(list(re.findall(r'(?<=0)[0-9]+(?!0)0', str(lims[0]))))
