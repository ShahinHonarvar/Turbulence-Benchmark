
def palindrome_of_length_n(s):
    return {x for x in set(re.findall('(?i)[a-z]{445}', s)) if x == x[::-1]}
