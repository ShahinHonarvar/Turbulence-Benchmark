
def filter_chars(input_str):
    target_chars = set([c for i,c in enumerate(input_str) if 10 <= i <= 52 and '@' <= c <= 'T'])
    return ''.join([c for c in input_str if c not in target_chars])
