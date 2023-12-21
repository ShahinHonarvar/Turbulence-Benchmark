from Q34.command_results_4.Folder_58.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(733):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(733):
        l.append({i})
    assert find_original_set(*l) == set(range(733))


def test_similar_sets():
    l = []
    for i in range(733):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 733*733, 733):
        l.append(set(range(i, i + 733)))
    assert find_original_set(*l) == set(range(733*733))


def test_several_subsets():
    l = []
    for i in range(733):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(733))
