
def palindrome_of_length_n(s):
    return {x for x in re.findall(r'[a-zA-Z]{420}', s) if x == x[::-1]}
