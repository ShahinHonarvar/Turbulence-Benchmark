
def palindrome_of_length_at_least_n(string, n):
    return {x for x in re.findall(r'[A-Za-z]{63,}', string) if len(x) >= n and x == x[::-1]}
