
def palindrome_of_length_at_least_n(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive search
    palindromes = set()  # Create a set to store the palindromes
    for i in range(len(s)):  # Loop through each position in the string
        for j in range(i+5, len(s)+1):  # Loop through each position after the current one and check if it is a palindrome
            if s[i:j] == s[i:j][::-1]:  # Check if the substring from i to j is a palindrome
                palindromes.add(s[i:j])  # If it is, add it to the set of palindromes
    return palindromes  # Return the set of palindromes
