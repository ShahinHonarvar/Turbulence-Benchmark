
def palindrome_of_length_n(string):
    palindromes = set()
    length = 20
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
