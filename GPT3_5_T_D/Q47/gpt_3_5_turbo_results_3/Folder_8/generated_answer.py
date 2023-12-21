
def palindromes_of_specific_lengths(s):
    substr = s[17:73].lower()
    palindromes = set()
    
    for i in range(len(substr)):
        for length in range(50, 52):
            if i + length <= len(substr):
                sub = substr[i:i+length]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    
    return palindromes
