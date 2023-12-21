
def palindromes_between_indices(string):
    # Create a list of all English letters in the string
    letter_list = []
    for char in string:
        if char.isalpha():
            letter_list.append(char)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over all possible starting positions for a palindrome
    for i in range(3, 9):
        # Iterate over all possible ending positions for a palindrome
        for j in range(i, 9):
            # Check if the substring starting at position i and ending at position j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    return palindromes
