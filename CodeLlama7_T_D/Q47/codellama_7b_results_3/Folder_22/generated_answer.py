
def palindromes_of_specific_lengths(string):
    # Create a substring from index 100 to index 200, both inclusive
    substring = string[100:200]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(substring)):
        # Check if the character is a letter (i.e., not a whitespace or a punctuation)
        if substring[i].isalpha():
            # Create a string with the same length as the substring, starting from the current character
            temp_string = substring[i:]

            # Check if the string is a palindrome (i.e., it reads the same backwards and forwards)
            if temp_string == temp_string[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(temp_string)

    # Iterate through each palindrome in the set and check if its length is between 5 and 10 (both inclusive)
    for palindrome in palindromes:
        if len(palindrome) >= 5 and len(palindrome) <= 10:
            # Add the palindrome to a new set of palindromes with lengths between 5 and 10 (both inclusive)
            filtered_palindromes.add(palindrome)
    # Return the set of palindromes with lengths between 5 and 10 (both inclusive)
    return filtered_palindromes
