
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in range(8, 10):
        for j in range(i+2, len(string)):
            if string[i] == string[j]:
                substr = string[i:j+1]
                if substr[::-1] in palindromes:
                    continue
                if all(letter in substr for letter in letters):
                    palindromes.add(substr)
    
    return palindromes
