
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    
    for i in range(len(s)):
        for j in range(i+445, len(s)+1):
            substring = s[i:j]
            if len(substring) == 445 and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    
    return result
