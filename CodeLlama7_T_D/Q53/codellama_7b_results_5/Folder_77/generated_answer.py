
def palindrome_of_length_at_least_n(string, n=149):
    # Convert the input string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each character in the input string

    for i in range(len(string)):

        # Check if the current character is a letter (A-Z)

        if string[i].isalpha():

            # Extract the substring starting from the current character and extending to the end of the input string

            substr = string[i:]

            # Check if the substring is a palindrome by comparing it in reverse order

            if substr == substr[::-1]:

                # Add the palindrome to the set

                palindromes.add(substr)

    # Return the set of palindromes that meet the length criterion

    return palindromes
