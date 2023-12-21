
def palindromes_of_specific_lengths(string):
    substr = string[18:99].lower()
    palindromes = set()
    for length in range(31, 52):
        for start in range(len(substr) - length + 1):
            part = substr[start : start + length]
            if part == part[::-1] and part.isalpha():
                palindromes.add(part)
    return palindromes
