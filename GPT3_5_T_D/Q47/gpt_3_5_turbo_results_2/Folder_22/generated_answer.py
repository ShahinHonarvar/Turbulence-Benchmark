
def palindromes_of_specific_lengths(string):
    substring = string[100:201].lower()
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(5, 11):
            if i + j <= len(substring):
                sub = substring[i:i+j]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    
    return palindromes
