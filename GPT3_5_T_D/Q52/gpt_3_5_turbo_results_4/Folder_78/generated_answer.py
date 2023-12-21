
def palindrome_of_length_n(string):
    palindromes = set()
    
    # remove non-English letters from the string
    string = ''.join([char for char in string if char.isalpha()])
    
    # iterate through all possible substrings of length 48 in the string
    for i in range(len(string)-47):
        substring = string[i:i+48]
        
        # check if the substring is a palindrome
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
