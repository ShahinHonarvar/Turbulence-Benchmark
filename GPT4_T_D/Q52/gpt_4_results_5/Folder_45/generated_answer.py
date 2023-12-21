
def palindrome_of_length_n(string):
    string = string.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    string = "".join([c for c in string if c in valid_chars])
    
    palindromes = set()
    for i in range(len(string) - 20):
        subset = string[i:i+21]
        if subset == subset[::-1]:
            palindromes.add(subset)
    return palindromes
