
def palindromes_of_specific_lengths(string):
    # Create a substring from index 10 to index 59 (both inclusive)
    sub_string = string[10:60]
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(sub_string)):
        # Get the current character and its corresponding reverse character
        char = sub_string[i]
        rev_char = sub_string[len(sub_string) - 1 - i]
        # Check if the current character is a palindrome of length between 18 to 36 (both inclusive)
        if len(char + rev_char) in range(18, 37):
            # Add the palindrome to the set
            palindromes.add(char + rev_char)
    return palindromes
