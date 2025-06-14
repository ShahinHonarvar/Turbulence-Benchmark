
def palindromes_of_specific_lengths(string):
    # Get substring from index 10 to 74, both inclusive
    substr = string[10:75]
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a letter
        if substr[i].isalpha():
            # Get the length of the palindrome from the current index
            length = len(substr) - i
            
            # Check if the length is between 6 and 8 (inclusive)
            if 6 <= length <= 8:
                # Create a substring from the current index to the end of the substr
                sub_substr = substr[i:]
                
                # Check if the substring is a palindrome
                if sub_substr == sub_substr[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(sub_substr)
    
    return palindromes
