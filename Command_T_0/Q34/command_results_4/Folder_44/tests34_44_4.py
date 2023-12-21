from Q34.command_results_4.Folder_44.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(926):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(926):
        l.append({i})
    assert find_original_set(*l) == set(range(926))


def test_similar_sets():
    l = []
    for i in range(926):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 926*926, 926):
        l.append(set(range(i, i + 926)))
    assert find_original_set(*l) == set(range(926*926))


def test_several_subsets():
    l = []
    for i in range(926):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(926))
