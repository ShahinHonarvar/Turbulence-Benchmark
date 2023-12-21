
def palindrome_of_length_n(string):
    palindromes = set()
    length = 51
    
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        lowercase_substring = substring.lower()
        if lowercase_substring == lowercase_substring[::-1] and lowercase_substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
