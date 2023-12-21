
def palindrome_of_length_n(string):
    return {x for x in re.findall(r'[a-zA-Z]{25}', string, flags=re.IGNORECASE) if x == x[::-1]}
