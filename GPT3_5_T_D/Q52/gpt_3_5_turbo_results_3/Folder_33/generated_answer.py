
def palindrome_of_length_n(string):
    length = 475
    palindrome_set = set()
    
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        substr_lower = substr.lower()
        
        if substr_lower == substr_lower[::-1] and substr_lower.isalpha():
            palindrome_set.add(substr)
    
    return palindrome_set
