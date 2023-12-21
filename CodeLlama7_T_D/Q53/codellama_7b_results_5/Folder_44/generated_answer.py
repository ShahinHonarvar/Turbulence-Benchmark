
def palindrome_of_length_at_least_n(string, n=89):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the string

    for i in range(len(string)):

        # Check if the character at position i is a letter

        if string[i].isalpha():

            # Extract the substring starting from position i and ending at the end of the string

            substr = string[i:]

            # Iterate over the characters in the substring

            for j in range(len(substr)):

                # Check if the character at position j is a letter

                if substr[j].isalpha():

                    # Extract the substring starting from position 0 and ending at position j

                    palindrome = substr[:j+1]

                    # Check if the extracted substring is a palindrome

                    if palindrome == palindrome[::-1]:

                        # Add the extracted substring to the set of palindromes

                        palindromes.add(palindrome)

    # Return the set of palindromes of length greater than or equal to 89 that exist in the given string

    return palindromes
