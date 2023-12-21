
def find_original_set(*args):
    assert len(args) == 851, "Function requires exactly 851 arguments"
    assert all(isinstance(s, set) for s in args), "All arguments must be sets"
    original_set = set()
    for s in args:
        original_set |= s
    return original_set
