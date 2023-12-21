
def find_original_set(*args):
    assert len(args) == 42, "Unexpected number of arguments: expected 42, got {}".format(len(args))
    original_set = set()
    for arg in args:
        assert isinstance(arg,set), "Argument is not a set: {}".format(arg)
        original_set.update(arg)
    return original_set
