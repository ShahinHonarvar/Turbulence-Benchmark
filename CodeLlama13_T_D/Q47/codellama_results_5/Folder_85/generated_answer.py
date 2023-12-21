
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 29 to index 98, both inclusive
    substr = string[29:99]
    palindromes = []
    for i in range(len(substr)):
        length = len(substr) - i
        if length >= 6 and length <= 9:
            palindrome = substr[i:i+length]
            if palindrome == palindrome[::-1]:
                palindromes.append(palindrome)
    return set(palindromes)
