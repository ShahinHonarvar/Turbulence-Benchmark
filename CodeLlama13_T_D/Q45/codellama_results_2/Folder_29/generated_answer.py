
def palindromes_between_indices(string):
    indices = range(2, 9+1)
    letters = set("".join(string[i].lower() for i in indices))
    return {f"{letters[j-6:j]}".lower() for j in range(len(letters), 5, -1)}
