
def palindrome_of_length_at_least_n(s):
    return {p for p in set(re.findall('[a-zA-Z]{34,}', s)) if p == p[::-1]}
