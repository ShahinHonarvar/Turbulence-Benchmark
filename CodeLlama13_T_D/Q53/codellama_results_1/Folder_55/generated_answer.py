
def palindrome_of_length_at_least_n(s):
    return {x for x in re.findall(r'(\w{83,})', s, flags=re.IGNORECASE) if x == x[::-1]}
