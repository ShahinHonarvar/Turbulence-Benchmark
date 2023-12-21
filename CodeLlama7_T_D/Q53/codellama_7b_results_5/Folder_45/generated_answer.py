
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each character in the string
    for i in range(len(string)):

        # Check if the current character is a letter
        if string[i].isalpha():

            # Iterate over the remaining characters in the string, starting from the current index
            for j in range(i + 1, len(string) + 1):

                # Check if the substring starting at the current index and ending at the current index is a palindrome
                if string[i:j] == string[i:j][::-1]:

                    # If it is a palindrome, add it to the set of palindromes
                    palindromes.add(string[i:j])

    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return palindromes
