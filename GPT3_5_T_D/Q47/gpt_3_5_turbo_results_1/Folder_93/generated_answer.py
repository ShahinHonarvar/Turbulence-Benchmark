
def palindromes_of_specific_lengths(string):
    substr = string[17:96]
    substr = substr.lower()
    palindromes = set()

    for length in range(13, 50):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
