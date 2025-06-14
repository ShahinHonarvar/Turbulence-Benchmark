
def palindromes_between_indices(string):
    # Convert string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the given string
    for i in range(7, 10):
        # Check if the current character is a letter or not
        if string[i].isalpha():
            # If it is a letter, check if the current character and its counterpart are both letters
            if string[i - 3].isalpha() and string[i + 3].isalpha():
                # If they are both letters, check if the current character is the same as its counterpart
                if string[i] == string[i - 3]:
                    # If it is the same, add the palindrome to the set of palindromes
                    palindromes.add(string[i - 3:i + 3])
    return palindromes
