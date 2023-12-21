
def palindrome_of_length_at_least_n(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is an English letter
        if string[i].isalpha():
            # If it is, check if the substring starting from that character is a palindrome
            if string[i:] == string[i:][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:])
    
    return palindromes
