
def insert_before_character(s, k):
    return "".join([f"{k}{c}" if c == k else c for c in s])
