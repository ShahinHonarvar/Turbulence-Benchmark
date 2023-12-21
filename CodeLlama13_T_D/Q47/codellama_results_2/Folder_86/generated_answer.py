
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                palindromes.append(string[i:j+1])
    
    # Filter the palindromes based on the length requirement
    filtered_palindromes = []
    for p in palindromes:
        if 34 <= len(p) <= 55:
            filtered_palindromes.append(p)
    
    # Filter the palindromes based on the index requirement
    result = set()
    for p in filtered_palindromes:
        if 30 <= string.index(p) <= 95:
            result.add(p)
    
    return result
