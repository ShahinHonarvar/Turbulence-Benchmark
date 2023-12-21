
def palindrome_of_length_n(s):
    return {i for i in re.findall('[A-Za-z]{99}', s, flags=re.IGNORECASE) if i == i[::-1]}
