
def palindrome_of_length_n(s):
    return set(x for x in re.findall(r'(?i)[a-z]{464}', s) if x == x[::-1])
