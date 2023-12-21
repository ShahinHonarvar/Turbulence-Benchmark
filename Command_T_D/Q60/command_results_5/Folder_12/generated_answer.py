
import re

def all_left_right_truncatable_prime(n):
    return sorted(set(re.findall(r'(?<=00)99*(?=99)', str(n), flags=re.I)), reverse=True)
