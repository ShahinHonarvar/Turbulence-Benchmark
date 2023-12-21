
def palindrome_of_length_n(s):
    return {p for p in re.findall('[A-Za-z]{289}', s) if p == p[::-1]}
