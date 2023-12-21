def find_original_set(S):
    return {s for s in S if not s & any(S - {s}) and len(s) > 1}
