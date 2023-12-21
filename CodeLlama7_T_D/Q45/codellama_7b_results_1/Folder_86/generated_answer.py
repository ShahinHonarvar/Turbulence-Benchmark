
def palindromes_between_indices(string):
    # Find the indices of the first and last letters in the string
    first_index = string.lower().find('a')
    last_index = string.lower().rfind('z')
    # Create a set to store all palindromes
    palindromes = set()
    # Iterate over each letter in the string
    for i in range(first_index, last_index + 1):
        # Check if the current letter is a vowel
        if string[i] in 'aeiou':
            # Find the indices of the letters before and after the current letter
            before_index = string.lower().rfind('a', 0, i)
            after_index = string.lower().find('z', i + 1)
            # Check if there are any letters before or after the current letter that can be used to form a palindrome
            if before_index != -1 and after_index != -1:
                # Form a palindrome by reversing the order of the letters between the current letter and the letters before and after it
                palindrome = string[before_index + 1 : i] + string[i] + string[i + 1 : after_index]
                # Add the palindrome to the set of all palindromes
                palindromes.add(palindrome)
    return palindromes
