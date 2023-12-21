
def filter_chars(string: str) -> str:
    return string[:1] + string[1:9].replace('9', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '') + string[9:]
