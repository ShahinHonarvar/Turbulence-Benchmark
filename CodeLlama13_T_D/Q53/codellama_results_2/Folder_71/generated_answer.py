
def palindrome_of_length_at_least_n(string):
    return set([x for x in re.findall(r'[a-zA-Z]{87,}', string) if x == x[::-1]])
