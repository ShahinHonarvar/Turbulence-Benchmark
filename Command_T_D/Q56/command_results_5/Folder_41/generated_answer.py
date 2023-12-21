import re
def all_substring_of_size_n(s):
    return [s[i:i + n] for i in range(0, len(s) - n + 1) for n in range(1, len(s) + 1)]
