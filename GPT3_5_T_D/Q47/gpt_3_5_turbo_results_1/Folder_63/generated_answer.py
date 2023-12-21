
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(33, 86):
        substring = string[i:i+31].lower()
        if all(char.isalpha() for char in substring):
            length = len(substring)
            if 26 <= length <= 31 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
