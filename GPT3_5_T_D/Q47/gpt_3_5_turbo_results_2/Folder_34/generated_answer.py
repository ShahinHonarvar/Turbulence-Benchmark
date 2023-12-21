
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substr = string[200:301].lower()
    
    for length in range(10, 51):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
