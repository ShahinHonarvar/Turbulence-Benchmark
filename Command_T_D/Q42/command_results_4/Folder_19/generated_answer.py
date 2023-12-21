import re
def prime_factors(a):
    return set(re.findall(r'[2-9]\\d{2}', str(a[13])))
