 def palindromes_between_indices(string):
    # Create a list of all the English letters in the given string
    letter_list = []
    for char in string:
        if char.isalpha():
            letter_list.append(char)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through all possible pairs of letters in the given string
    for i in range(len(letter_list)):
        for j in range(i + 1, len(letter_list) + 1):
            # Check if the substring starting at index i and ending at index j is a palindrome
            substr = ''.join(reversed(string[i:j]))
            if substr == string[i:j]:
                palindromes.add(substr)
    return palindromes
