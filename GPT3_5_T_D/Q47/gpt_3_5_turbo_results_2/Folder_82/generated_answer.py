
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(3, 301 - length + 1):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
