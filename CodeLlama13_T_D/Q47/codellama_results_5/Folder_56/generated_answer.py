
def palindromes_of_specific_lengths(string):
    # Find all substrings of the given string that are palindromes and have a length between 3-7
    palindromes = set()
    for i in range(1, 9):
        for j in range(i+2, len(string)):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) >= 3 and len(substring) <= 7:
                palindromes.add(substring)
    return palindromes
