
def palindromes_of_specific_lengths(string):
    import re
    string = string[:21]
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for length in range(5, 81):
        for i in range(len(string)-length+1):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
