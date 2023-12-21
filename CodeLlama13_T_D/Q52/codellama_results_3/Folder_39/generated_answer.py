
def palindrome_of_length_n(string, n):
    return {s for s in re.findall(r"([a-zA-Z]{59})", string) if s == s[::-1]}
