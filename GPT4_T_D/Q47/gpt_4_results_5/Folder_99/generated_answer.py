
def palindromes_of_specific_lengths(string):
    string = string[127:289].lower()
    palindromes = set()
    for length in range(119, 142):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
