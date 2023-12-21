
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):

        # Check if the character at position i is a letter
        if string[i].isalpha():

            # Iterate over the remaining characters in the string from position i + 1 to the end
            for j in range(i + 1, len(string)):

                # Check if the substring starting at position i and ending at position j is a palindrome
                if string[i:j+1] == string[i:j+1][::-1]:

                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j+1])

    # Return the set of all palindromes of length 147 found in the given string
    return palindromes
