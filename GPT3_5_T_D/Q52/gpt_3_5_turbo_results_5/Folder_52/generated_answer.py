
def palindrome_of_length_n(string):
    palindrome_set = set()
    length = 423
    
    string = string.lower()
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
            
    return palindrome_set
