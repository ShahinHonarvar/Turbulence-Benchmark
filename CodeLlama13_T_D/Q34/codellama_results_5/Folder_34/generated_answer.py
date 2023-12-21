
def find_original_set(s1, s2, s3, ..., s95):
    return {x for x in range(min(s1), max(s95)) if all(x in si for si in (s1, s2, s3, ..., s95))}
