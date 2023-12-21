
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'([A-Za-z]{19})', s, flags=re.IGNORECASE) if p == p[::-1]}
