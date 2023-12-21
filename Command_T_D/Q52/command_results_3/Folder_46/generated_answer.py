import re
def palindrome_of_length_n(s):
    if not s:
        return set()
    for i in range(1, 463):
        if re.search(r'([a-z]{i})\1', s):
            return {re.sub(r'([a-z]{i})\1', '', s)}
    return set()
