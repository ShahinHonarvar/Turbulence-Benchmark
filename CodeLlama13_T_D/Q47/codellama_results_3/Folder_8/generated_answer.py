
def palindromes_of_specific_lengths(string):
    length = len(string)
    if length < 72 or length > 17:
        return set()
    
    substring = string[17:73]
    palindromes = set()
    
    for i in range(50, 52):
        for j in range(length - i + 1):
            word = substring[j:j+i]
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
