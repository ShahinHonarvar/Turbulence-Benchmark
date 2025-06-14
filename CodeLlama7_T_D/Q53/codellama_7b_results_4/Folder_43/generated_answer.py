 def palindrome_of_length_at_least_n(string, n=49):
    # Convert the input string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the input string

    for i in range(len(string)):

        # Check if the character at position 'i' is a letter

        if string[i].isalpha():

            # Extract the substring starting from index 'i' and ending at the end of the string

            substr = string[i:]

            # Iterate over the characters in the extracted substring

            for j in range(len(substr)):

                # Check if the character at position 'j' is a letter

                if substr[j].isalpha():

                    # Extract the substring starting from index '0' and ending at index 'j'

                    substr_rev = substr[:j+1]

                    # Check if the extracted substring is a palindrome

                    if substr_rev == substr_rev[::-1]:

                        # Add the extracted substring to the set of palindromes

                        palindromes.add(substr_rev)

    # Return the set of all palindromes of length greater than or equal to 49 that exist in the given string, if any

    return palindromes
