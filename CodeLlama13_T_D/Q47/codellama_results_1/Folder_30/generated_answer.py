
def palindromes_of_specific_lengths(string):
    substr = string[14:91]
    lengths = range(55, 72)
    palindromes = set()
    for length in lengths:
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
