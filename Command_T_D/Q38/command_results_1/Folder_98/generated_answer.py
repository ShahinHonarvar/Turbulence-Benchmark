import functools
def find_subset_of_length_n(s):
    return functools.reduce(
        functools.reduce,
        [
            functools.reduce(
                functools.reduce,
                [
                    functools.reduce(
                        functools.reduce,
                        [0] * n + [1] + [0] * n,
                    ),
                ] * n,
            )
            for n in range(1, len(s) + 1),
        ],
    )
