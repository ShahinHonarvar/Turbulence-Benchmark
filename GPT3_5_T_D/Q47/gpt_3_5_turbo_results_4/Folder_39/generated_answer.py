
def palindromes_of_specific_lengths(string):
    substring = string[31:92]
    palindrome_set = set()
    
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            sub_string = substring[i:i+length]
            if sub_string.lower() == sub_string.lower()[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string)
    
    return palindrome_set
