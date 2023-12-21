
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    
    for i in range(length):
        for j in range(i + 6, length + 1):
            subset = s[i:j]
            if subset == subset[::-1]:
                if all(character.isalpha() for character in subset):
                    palindromes.add(subset)
    
    return palindromes
