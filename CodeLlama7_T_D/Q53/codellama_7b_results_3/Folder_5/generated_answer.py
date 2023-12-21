
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Loop through each character in the reverse of the string
            for j in range(len(string)-1, -1, -1):
                # Check if the character is a letter
                if string[j].isalpha():
                    # Check if the characters are the same
                    if string[i].lower() == string[j].lower():
                        # If the length of the palindrome is greater than or equal to n, add it to the set
                        if len(string[i:j+1]) >= n:
                            palindromes.add(string[i:j+1])
    return palindromes
