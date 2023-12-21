
def palindromes_of_specific_lengths(string):
    substring = string[10:56]
    substring = substring.lower()
    palindromes = set()
    
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
