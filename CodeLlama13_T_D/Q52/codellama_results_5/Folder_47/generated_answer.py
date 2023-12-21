
def palindrome_of_length_n(s):
    return {p for p in re.findall('[a-zA-Z]{34}', s, flags=re.IGNORECASE) if p == p[::-1]}
