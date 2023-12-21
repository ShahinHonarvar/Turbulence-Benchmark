
def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[:5]
    substr_palindromes = set()
    
    for i in range(0, len(substr)):
        for j in range(i+3, min(i+5, len(substr))+1):
            sub_sub_str = substr[i:j]
            if sub_sub_str == sub_sub_str[::-1] and sub_sub_str.isalpha():
                substr_palindromes.add(sub_sub_str)
                
    return substr_palindromes
