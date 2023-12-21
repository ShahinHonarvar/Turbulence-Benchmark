
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 10):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the string without the current character
            no_current = string[:i] + string[i+1:]
            # Loop through each character in the copied string
            for j in range(4, 10):
                # Check if the current character is a letter
                if no_current[j].isalpha():
                    # Create a palindrome by reversing the order of the letters
                    palindrome = "".join(reversed(no_current[i:j+1]))
                    # Check if the palindrome has at least 4 letters and add it to the set
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes
