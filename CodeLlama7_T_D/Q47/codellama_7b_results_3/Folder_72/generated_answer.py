
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(26, 90 + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the reversed substring
            for j in range(i, 26 - 1, -1):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # If the current character and its reverse are both letters, add the palindrome to the set
                    palindromes.add(string[i:j+1])
    return palindromes
