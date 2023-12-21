
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substr = string.lower()[20:75]
    for length in range(36, 43):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
