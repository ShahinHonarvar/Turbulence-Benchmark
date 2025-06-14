
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 7):
        substring = string[i:i + 7]
        if len(substring) < 7:
            break
        if all([letter.lower() in "abcdefghijklmnopqrstuvwxyz" for letter in substring]):
            palindromes.add("".join(reversed(substring)))
    return palindromes
