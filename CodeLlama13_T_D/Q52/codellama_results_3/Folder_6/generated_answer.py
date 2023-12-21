
def palindrome_of_length_n(string, n):
    return {x for x in re.findall(r'(?i)(?<![aeiouAEIOU])([a-zA-Z]{474})(?!\1)', string)}
