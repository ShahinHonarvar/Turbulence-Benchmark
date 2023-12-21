
def palindromes_between_indices(input_string):
    # Check if the input string is empty
    if not input_string:
        return set()

    # Get the length of the input string
    input_length = len(input_string)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each possible starting index in the range [3, 9]
    for i in range(3, 10):
        # Check if the starting index is valid
        if i >= input_length:
            continue

        # Get the substring of the input string that starts at the current starting index
        substring = input_string[i:]

        # Loop through each possible ending index in the range [3, 9]
        for j in range(3, 10):
            # Check if the ending index is valid
            if j >= input_length - i:
                continue

            # Get the substring of the input string that ends at the current ending index
            substring = input_string[i:j + i]

            # Check if the substring is a palindrome in a case-insensitive manner
            if substring.lower() == substring[::-1].lower():
                # Add the substring to the set of palindromes
                palindromes.add(substring)

    # Return the set of palindromes that meet the specified criteria
    return palindromes
