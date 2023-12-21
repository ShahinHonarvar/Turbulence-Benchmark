
def palindromes_of_specific_lengths(s):
    s = s[30:96]
    result = set()
    
    for len_sub in range(34, 56):
        for i in range(len(s) - len_sub + 1):
            substring = s[i:i+len_sub]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(s[i:i+len_sub])
            
    return result
