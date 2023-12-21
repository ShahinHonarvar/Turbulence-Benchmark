def palindromes_between_indices(s):
    return set(f"".join(sorted(set(str(s)[2:-2]))) for i in range(3, 8))
