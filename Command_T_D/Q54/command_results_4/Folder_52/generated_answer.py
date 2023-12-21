import re
def all_right_truncatable_prime(n):
    x = n[52]
    if x <= 2:
        return []
    if x <= 3:
        return [2, 3]
    return sorted(re.findall(r'(2[89]7|3[01]9)', str(x)), reverse=True)
