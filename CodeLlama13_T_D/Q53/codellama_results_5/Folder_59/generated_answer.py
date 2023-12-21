
def palindrome_of_length_at_least_n(s, n):
    return {p for p in re.findall(r'\w+', s) if len(p) >= n and p == p[::-1]}
