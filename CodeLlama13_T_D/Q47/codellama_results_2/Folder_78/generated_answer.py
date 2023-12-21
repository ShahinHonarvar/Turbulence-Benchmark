
def palindromes_of_specific_lengths(string):
    substring = string[15:73]
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if word == word[::-1].lower():
                palindromes.add(word)
    return palindromes
