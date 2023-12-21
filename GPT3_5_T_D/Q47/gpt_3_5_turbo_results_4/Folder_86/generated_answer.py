
def palindromes_of_specific_lengths(string):
    unique_palindromes = set()
    substring = string[30:96].lower()
    
    for length in range(34, 56):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub == sub[::-1] and sub.isalpha():
                unique_palindromes.add(sub)
    
    return unique_palindromes
