import itertools
def find_original_set(s1, s2, s3):
    def helper(s1, s2, s3):
        return {x for x in itertools.chain.from_iterable(s1, s2, s3) if not any(x not in y for y in (s1, s2, s3))}
    return helper(s1, s2, s3)
