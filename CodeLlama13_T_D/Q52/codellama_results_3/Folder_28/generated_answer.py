
def palindrome_of_length_n(string, n):
    return {substr for substr in re.findall('[a-zA-Z]{' + str(n) + '}', string) if substr == substr[::-1]}
