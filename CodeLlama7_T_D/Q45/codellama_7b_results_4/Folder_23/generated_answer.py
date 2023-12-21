
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Get the index of the next character that is not a letter
        j = i + 1
        while j < len(s) and not s[j].isalpha():
            j += 1
        # If we reached the end of the string, break out of the loop
        if j == len(s):
            break
        # Get the index of the previous character that is not a letter
        k = i - 1
        while k >= 0 and not s[k].isalpha():
            k -= 1
        # If we reached the beginning of the string, break out of the loop
        if k < 0:
            break
        # Get the substring between the two indices
        substr = s[i:j]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
