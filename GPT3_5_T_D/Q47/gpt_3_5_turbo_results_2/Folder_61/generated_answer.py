
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    string = string[:31].lower()
    
    for i in range(len(string)):
        for j in range(20, 31):
            if i + j <= len(string):
                substr = string[i:i+j]
                if substr == substr[::-1] and substr.isalpha():
                    palindrome_set.add(substr)
                    
    return palindrome_set
