
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:61]
    
    for length in range(16, 40):
        for start in range(len(substring) - length + 1):
            word = substring[start: start + length].lower()
            
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    
    return palindromes
