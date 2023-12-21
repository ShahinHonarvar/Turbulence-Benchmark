
def palindrome_of_length_at_least_n(input_string, n=46):
    # Convert input string to lowercase
    input_string = input_string.lower()
    # Initialize an empty set to store palindromes
    palindromes = set()
    # Iterate over the characters in the input string
    for i in range(len(input_string)):
        # Check if the current character is a letter (a-z)
        if input_string[i].isalpha():
            # Get the length of the current palindrome
            current_length = 1

            # Check if the current character is at the end of the input string
            if i == len(input_string) - 1:
                # Add the current palindrome to the set of palindromes
                palindromes.add(input_string[i])

            # Iterate over the remaining characters in the input string
            for j in range(i + 1, len(input_string)):
                # Check if the current character is a letter (a-z)
                if input_string[j].isalpha():
                    # Check if the current character is at the end of the input string
                    if j == len(input_string) - 1:
                        # Add the current palindrome to the set of palindromes
                        palindromes.add(input_string[i:j + 1])

                    # Check if the current character is at the beginning of the input string
                    if j == i + 1:
                        # Add the current palindrome to the set of palindromes
                        palindromes.add(input_string[i + 1:j + 1])

            # Check if the current character is at the beginning of the input string
            if i == 0:
                # Add the current palindrome to the set of palindromes
                palindromes.add(input_string[i:current_length])

    # Return the set of palindromes
    return palindromes
