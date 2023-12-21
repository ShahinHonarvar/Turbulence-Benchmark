
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall(r'[a-z]{4,}', s.lower()) if p == p[::-1]}
