
import string

def palindromes_of_specific_lengths(string):
    result = set()
    
    substring = string[62:89].lower()
    
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            current_palindrome = substring[i:i+length]
            if current_palindrome == current_palindrome[::-1] and all(char in string.ascii_letters for char in current_palindrome):
                result.add(current_palindrome)
    
    return result
