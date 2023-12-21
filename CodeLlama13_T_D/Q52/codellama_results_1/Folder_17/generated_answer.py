
def palindrome_of_length_n(s):
    s = s.lower()  # convert string to lowercase
    n = len(s)  # get length of input string
    palindromes = set()  # initialize empty set for palindromes
    
    for i in range(0, n - (n % 2)):
        # iterate over all possible starting indices for a palindrome
        for j in range(i + 1, n - (n % 2) + 1):
            # iterate over all possible ending indices for a palindrome
            if s[i:j] == s[i:j][::-1]:
                # check if substring is palindrome
                palindromes.add(s[i:j])
    
    return palindromes  # return set of all found palindromes
