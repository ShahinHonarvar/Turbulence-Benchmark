
def palindrome_of_length_at_least_n(string):
    import re
    string = string.lower()
    string = re.sub('[^a-z]', '', string)
    length = len(string)
    palindromes = set()
    
    for l in range(47, length + 1):
        for i in range(length - l + 1):
            substring = string[i:i + l]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
