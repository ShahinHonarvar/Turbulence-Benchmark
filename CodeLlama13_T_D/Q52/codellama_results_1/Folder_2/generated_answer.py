
def palindrome_of_length_n(string, n):
    return {s for s in re.findall(r'\b[a-zA-Z]{' + str(n) + '}\b', string)}
