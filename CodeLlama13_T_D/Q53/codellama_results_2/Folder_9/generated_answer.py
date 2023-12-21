
def palindrome_of_length_at_least_n(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is an English letter
        if string[i].isalpha():
            # Find the palindrome starting from this character
            palindrome = find_palindrome(string, i)
            
            # If a palindrome is found, add it to the set of palindromes
            if palindrome:
                palindromes.add(palindrome)
    
    return palindromes

def find_palindrome(string, start):
    # Initialize the current palindrome as an empty string
    palindrome = ""
    
    # Loop through each character in the string, starting from the given index
    for i in range(start, len(string)):
        # Check if the current character is an English letter
        if string[i].isalpha():
            # Add the current character to the palindrome
            palindrome += string[i]
            
            # Check if the palindrome is a valid palindrome
            if palindrome == palindrome[::-1]:
                return palindrome
    
    # If no palindrome is found, return an empty string
    return ""
