
def palindromes_between_indices(string):
    # Create a list of all English letters in the given string
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char)
    # Create a set to store all palindromes of length 4 or more
    palindromes = set()
    # Iterate over all possible pairs of English letters in the given string
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            # Create a palindrome by joining the two letters together in both orders
            palindrome = ''.join([letters[i], letters[j]])
            if palindrome == palindrome[::-1]:
                # Add the palindrome to the set of palindromes, unless it is already present
                if palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes
