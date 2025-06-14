 def palindrome_of_length_n(string):
    # Split the string into individual characters
    chars = string.split('')
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n
    for i in range(len(chars) - 130):
        # Check if the substring is a palindrome
        if chars[i:i+131] == chars[i:i+131][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(chars[i:i+131])
    return palindromes
