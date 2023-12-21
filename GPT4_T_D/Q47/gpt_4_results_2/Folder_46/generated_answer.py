
def palindromes_of_specific_lengths(inp_str):
    substr = inp_str[11:98]
    low = 29
    high = 62
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + low, min(i + high + 1, len(substr) + 1)):
            slice = substr[i:j]
            if slice.lower() == slice[::-1].lower() and slice.isalpha():
                palindromes.add(slice)
    return palindromes
