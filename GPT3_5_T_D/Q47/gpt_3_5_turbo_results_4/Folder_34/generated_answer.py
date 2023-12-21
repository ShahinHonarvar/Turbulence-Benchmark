
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(10, 51):
        for start in range(199, 301-length):
            substring = string[start:start+length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
