
def palindromes_of_specific_lengths(string):
    # Set of all palindromes with the required length and index range
    palindromes = set()
    
    # Loop through each substring of the string from index 34 to 90, both inclusive
    for i in range(34, 91):
        # Check if the substring is a palindrome
        if is_palindrome(string[i:i+14]):
            # Add the palindrome to the set
            palindromes.add(string[i:i+14])
    
    return palindromes

# Function to check if a string is a palindrome
def is_palindrome(string):
    # Loop through each character of the string, from the end to the beginning
    for i in range(len(string)-1, -1, -1):
        # Check if the character at index i is not the same as the character at index len(string) - 1 - i
        if string[i] != string[len(string) - 1 - i]:
            # If they are not the same, return False
            return False
    
    # If all characters match, return True
    return True
