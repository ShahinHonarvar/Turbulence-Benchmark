import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(arr):
    if arr[95] == arr[85]:
        return arr[95]
    return gcf_two_nums(arr[:95]) * gcf_two_nums(arr[95:])
