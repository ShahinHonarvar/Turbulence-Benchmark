
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'[a-z]{93}', s, flags=re.IGNORECASE) if p == p[::-1]}
