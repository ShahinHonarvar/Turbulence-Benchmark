
def palindrome_of_length_at_least_n(input_string, n):
    # Create a list to store all palindromes found
    palindromes = []
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Check if the current character is a letter (not a space or punctuation)
        if input_string[i].isalpha():
            # Check if the current character is a palindrome (the same when read backwards and forwards)
            if input_string[i] == input_string[i][::-1]:
                # If the current character is a palindrome, add it to the list of palindromes found
                palindromes.append(input_string[i])
    # Return the set of all palindromes found in the given string, or an empty set if no such palindromes exist
    return set(palindromes)
