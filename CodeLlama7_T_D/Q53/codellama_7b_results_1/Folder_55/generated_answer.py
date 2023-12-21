
def palindrome_of_length_at_least_n(string, n=83):
    # Create a dictionary to store the palindromes
    palindromes = {}

    # Iterate over each character in the string
    for i in range(len(string)):

        # Check if the character is an English letter
        if string[i].isalpha():

            # Create a copy of the string without the current character
            new_string = string[:i] + string[i+1:]

            # Iterate over each substring in the new string
            for j in range(len(new_string)):

                # Check if the substring is a palindrome
                if new_string[j:].lower() == new_string[j:].lower()[::-1]:

                    # Add the palindrome to the dictionary
                    palindromes.setdefault(new_string[j:], []).append(i)

    # Return the set of all palindromes of length greater than or equal to 83 that exist in the given string
    return set(palindromes)
