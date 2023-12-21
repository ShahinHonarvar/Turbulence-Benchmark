
def palindrome_of_length_n(string):
    return set(re.findall(r'[a-zA-Z]{3}', string, flags=re.IGNORECASE))
