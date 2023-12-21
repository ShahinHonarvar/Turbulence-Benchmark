
def palindrome_of_length_n(string):
    length = 63
    palindromes = set()
    string = string.lower()
    
    for i in range(len(string) - length + 1):
        sub_string = string[i:i+length]
        if sub_string == sub_string[::-1] and sub_string.isalpha():
            palindromes.add(sub_string)
    
    return palindromes
