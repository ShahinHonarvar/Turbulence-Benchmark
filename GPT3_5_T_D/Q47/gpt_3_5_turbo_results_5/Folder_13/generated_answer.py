
def palindromes_of_specific_lengths(string):
    start_index = 13
    end_index = 95
    palindromes = set()
    
    substring = string[start_index:end_index+1]
    
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    
    return palindromes
