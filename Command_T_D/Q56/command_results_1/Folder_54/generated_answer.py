import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    if len(s) == 1:
        yield s
    for i in range(1, min(len(s), 28)):
        for j in range(i + 1, min(len(s), 28)):
            for k in range(j + 1, min(len(s), 28)):
                yield ''.join(s[i:j+1])
                yield ''.join(s[i:k+1])
                yield ''.join(s[j:k+1])
                yield ''.join(s[i:])
