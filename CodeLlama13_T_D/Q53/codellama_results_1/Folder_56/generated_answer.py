
def palindrome_of_length_at_least_n(string):
    return set(re.findall('[A-Z]{84,}', string.lower()))
