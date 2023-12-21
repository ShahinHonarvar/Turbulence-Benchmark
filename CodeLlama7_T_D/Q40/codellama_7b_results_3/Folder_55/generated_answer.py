
def return_n_smallest_chars(s: str) -> List[str]:
    smallest_chars = sorted(s, key=lambda x: ord(x))[:75]
    return smallest_chars
