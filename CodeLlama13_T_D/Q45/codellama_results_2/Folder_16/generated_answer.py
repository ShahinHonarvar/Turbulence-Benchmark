
def palindromes_between_indices(string):
    # Set of possible English letters
    letters = set("abcdefghijklmnopqrstuvwxyz")
    # Set to store palindromes
    palindromes = set()
    
    for i in range(6, 10):
        # Generate all possible combinations of English letters between indices 6 and 9
        for combination in itertools.combinations(letters, i - 5):
            # Create a palindrome by combining the current combination with its reverse
            palindrome = "".join(combination + combination[::-1])
            # Check if the palindrome is a substring of the given string
            if palindrome in string:
                palindromes.add(palindrome)
    
    return palindromes
