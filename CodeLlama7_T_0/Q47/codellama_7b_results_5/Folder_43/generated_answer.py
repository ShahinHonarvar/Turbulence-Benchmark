
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 41
    end_index = 89
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = 23

            while length <= 38:
                # Check if the current character is a letter
                if string[i - length].isalpha():
                    # Check if the current character is the same as the previous character
                    if string[i - length] == string[i + length]:
                        # Add the palindrome to the set
                        palindromes.add(string[i - length:i + length])
                length += 1

    return palindromes
