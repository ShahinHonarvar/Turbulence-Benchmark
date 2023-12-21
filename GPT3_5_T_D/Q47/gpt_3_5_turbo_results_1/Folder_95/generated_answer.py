
def palindromes_of_specific_lengths(string):
    substring = string[12:57]
    palindromes = set()
    for i in range(len(substring) - 19):
        word = substring[i:i+20]
        if word == word[::-1] and word.isalpha():
            palindromes.add(word.lower())
    return palindromes
