
def palindromes_of_specific_lengths(string):
    substring = string[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
