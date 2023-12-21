
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(154, 183):
        for start in range(101, 293 - length + 1):
            substring = string[start - 1 : start + length - 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
