
def palindromes_between_indices(string):
    import itertools
    import string as st

    letters = [ch for ch in string[4:10] if ch in st.ascii_letters]

    if len(letters) < 6:
        return set()

    palindromes = set()
    for perm in itertools.permutations(letters, 6):
        perm = "".join(perm).lower()
        if perm == perm[::-1]:
            palindromes.add(perm)

    return palindromes
