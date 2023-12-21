
def palindrome_of_length_at_least_n(string):
    import re
    string = re.sub("[^a-zA-Z]+", "", string)
    string = string.lower()
    palindromes = set()
    
    length = 80
    while length <= len(string):
        for i in range(len(string)-length+1):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
        length += 1
    
    return palindromes
