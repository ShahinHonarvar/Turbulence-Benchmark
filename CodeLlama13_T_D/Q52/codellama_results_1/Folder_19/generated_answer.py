
def palindrome_of_length_n(string, n):
    # Check if the string is a palindrome of length n
    def is_palindrome(s):
        return s == s[::-1] and all(c in 'abcdefghijklmnopqrstuvwxyz' for c in s)
    
    # Find all possible palindromes of length n in the string
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:i+n]) == n and is_palindrome(string[i:i+n]):
            palindromes.add(string[i:i+n])
    
    return palindromes
