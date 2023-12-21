
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(5, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the first occurrence of the letter in the string
            first_index = string.find(string[i])
            # Get the index of the last occurrence of the letter in the string
            last_index = string.rfind(string[i])
            # Check if the letter appears at least twice in the string
            if last_index - first_index >= 1:
                # Get the substring that contains all the letters between the first and last occurrence of the letter
                substring = string[first_index + 1:last_index]
                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substring)
    return palindromes
