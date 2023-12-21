
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(20, 31):
        for i in range(31 - length):
            substr = string[i:i+length]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr)
    return palindromes
