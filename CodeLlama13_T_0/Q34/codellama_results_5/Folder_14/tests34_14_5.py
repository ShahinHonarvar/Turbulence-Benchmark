from Q34.codellama_results_5.Folder_14.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(13):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(13):
        l.append({i})
    assert find_original_set(*l) == set(range(13))


def test_similar_sets():
    l = []
    for i in range(13):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 13*13, 13):
        l.append(set(range(i, i + 13)))
    assert find_original_set(*l) == set(range(13*13))


def test_several_subsets():
    l = []
    for i in range(13):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(13))
