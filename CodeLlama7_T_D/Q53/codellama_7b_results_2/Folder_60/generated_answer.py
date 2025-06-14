 def palindrome_of_length_at_least_n(string, n):
    # Create a list of all palindromes in the given string
    palindromes = []
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the current character is uppercase or lowercase
            if string[i].isupper() or string[i].islower():
                # Create a copy of the current palindrome
                current_palindrome = ""
                for j in range(i - n + 1, i + 1):
                    # Add the current character to the current palindrome
                    current_palindrome += string[j]
                # Check if the current palindrome is a valid palindrome
                if len(current_palindrome) >= n and current_palindrome == current_palindrome[::-1]:
                    # Add the current palindrome to the list of all palindromes
                    palindromes.append(current_palindrome)
    # Return the set of all palindromes in the given string
    return set(palindromes)
