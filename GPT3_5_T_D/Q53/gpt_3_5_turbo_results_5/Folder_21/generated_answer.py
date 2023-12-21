
def palindrome_of_length_at_least_n(string):
    n = 112
    result = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    
    return result
