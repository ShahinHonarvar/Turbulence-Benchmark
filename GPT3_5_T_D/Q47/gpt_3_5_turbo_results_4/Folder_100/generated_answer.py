
def palindromes_of_specific_lengths(string):
    substring = string[29:97]
    substring = substring.lower()
    palindromes = set()
    
    for i in range(len(substring) - 11):
        for j in range(12, 19):
            word = substring[i:i+j]
            if word.isalpha() and word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
