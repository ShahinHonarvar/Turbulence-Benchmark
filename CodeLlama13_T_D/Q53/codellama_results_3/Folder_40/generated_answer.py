
def palindrome_of_length_at_least_n(s):
    return {p for p in set(re.findall(r'[a-zA-Z]{3,}', s)) if p == p[::-1]}
