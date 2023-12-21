
def palindromes_of_specific_lengths(string):
    substring = string[17:96]
    palindromes = set()
    
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            sub_lower = sub.lower()
            
            if sub_lower == sub_lower[::-1] and sub_lower.isalpha():
                palindromes.add(sub)
    
    return palindromes
