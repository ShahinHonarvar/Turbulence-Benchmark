
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    indices = range(1, 6)
    palindromes = set()
    
    for i in indices:
        for j in indices:
            if i == j: continue
            substr = string[i-1:j]
            reversed_substr = substr[::-1]
            
            if substr == reversed_substr and len(substr) >= 6:
                palindromes.add(substr)
    
    return palindromes
