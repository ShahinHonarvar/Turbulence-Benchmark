
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the results
    results = set()

    # Iterate over the substring from index 40 to index 94, both inclusive
    for i in range(40, 95):
        # Get the length of the current substring
        length = len(string[i:])

        # Check if the length is between 45 and 51 (both inclusive)
        if not (45 <= length <= 51):
            continue

        # Initialize a variable to store the palindrome
        palindrome = ""

        # Iterate over the characters of the substring
        for j in range(length):
            # Check if the current character is an English letter
            if not (string[i+j].isalpha() and string[i+j].islower()):
                break

            # Append the current character to the palindrome
            palindrome += string[i+j]

        # Check if the palindrome is a palindrome
        if palindrome == palindrome[::-1]:
            results.add(palindrome)

    # Return the set of all palindromes found
    return results
