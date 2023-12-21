
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    
    for i in range(len(s)):
        for j in range(i+40, len(s)+1):
            substr = s[i:j]
            if substr == substr[::-1] and all(char.isalpha() for char in substr):
                result.add(substr)
    return result
