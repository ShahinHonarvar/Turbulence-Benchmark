
def palindromes_of_specific_lengths(string):
    substring = string[10:101]
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            word = substring[start:start+length]
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes
