
def palindrome_of_length_at_least_n(input_string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the input string
    for i in range(len(input_string)):

        # Check if the current character is a letter
        if input_string[i].isalpha():

            # Get the length of the substring starting from the current character and ending at the end of the string
            substr_length = len(input_string) - i

            # Loop through each possible palindrome length between n and substr_length
            for j in range(n, substr_length + 1):

                # Get the substring starting from the current character and ending at the length of the palindrome
                substr = input_string[i:i + j]

                # Check if the substring is a palindrome
                if substr == substr[::-1]:

                    # Add the palindrome to the set
                    palindromes.add(substr)

    # Return the set of all palindromes that exist in the given string and have a length greater than or equal to n
    return palindromes
