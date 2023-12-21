
def palindromes_between_indices(string):
    indices = range(4, 7)
    substr = ''.join([char.lower() for char in string[indices[0]:indices[-1]+1] if char.isalpha()])
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+3, len(substr)+1):
            if substr[i:j] == substr[i:j][::-1]:
                palindromes.add(substr[i:j])
    return palindromes
