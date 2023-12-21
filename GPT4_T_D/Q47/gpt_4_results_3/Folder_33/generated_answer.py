
def palindromes_of_specific_lengths(s):
    s = s[130:296].lower()
    
    result = set()     
    for i in range(103, 159):
        for j in range(len(s) - i + 1):
            substring = s[j:j+i]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
