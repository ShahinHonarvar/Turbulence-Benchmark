
def palindromes_of_specific_lengths(string):
    substring = string[10:101]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
