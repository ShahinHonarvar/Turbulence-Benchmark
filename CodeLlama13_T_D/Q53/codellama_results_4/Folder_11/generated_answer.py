
def palindrome_of_length_at_least_n(s):
    return set(w for w in re.findall(r'\b\w+\b', s) if len(w) >= 54 and w == w[::-1])
