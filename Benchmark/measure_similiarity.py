import ast
from difflib import SequenceMatcher


def codes_similarity(tree1, tree2, flag=False):
    interesting_classes = ["List", "Tuple", "Set", "Dict", "Call", "Not", "BinOp", "Add", "Sub", "Mult", "Div",
                           "FloorDiv", "Mod", "Pow", "LShift", "RShift", "BitOr", "BitXor", "BitAnd", "MatMult",
                           "BoolOp", "And", "Or", "Compare", "Eq", "NotEq", "Lt", "LtE", "Gt", "GtE", "Is", "IsNot",
                           "In", "NotIn", "IfExp", "Subscript", "Index", "Slice", "ExtSlice", "ListComp", "SetComp",
                           "DictComp", "GeneratorExp", "Assign", "AnnAssign", "AugAssign", "Raise", "Assert", "Delete",
                           "Import", "ImportFrom", "If", "For", "While", "Break", "Continue", "Try", "TryFinally",
                           "TryExcept", "ExceptHandler", "With", "FunctionDef", "Lambda", "Return", "Yield",
                           "YieldFrom", "Nonlocal", "Global"]

    if flag:
        nodes1 = [node.__class__.__name__ for node in ast.walk(
            tree1) if node.__class__.__name__ in interesting_classes]
        nodes2 = [node.__class__.__name__ for node in ast.walk(
            tree2) if node.__class__.__name__ in interesting_classes]
    else:
        nodes1 = [node.__class__.__name__ for node in ast.walk(tree1)]
        nodes2 = [node.__class__.__name__ for node in ast.walk(tree2)]

    matcher = SequenceMatcher(None, nodes1, nodes2)
    similarity = matcher.ratio()

    return similarity


def find_index_of_similar_skeleton(bucket_skeletons, current_skeleton, threshold):
    for i in range(0, len(bucket_skeletons)):
        similarity_count = 0
        for tup in bucket_skeletons[i]:
            similarity = codes_similarity(current_skeleton, tup[1])
            if similarity >= threshold:
                similarity_count += 1

        if similarity_count == len(bucket_skeletons[i]):
            return i
    return None


def similarity_partition(programs, threshold):
    first_folder_number, first_program = programs[0]
    bucket_skeletons = [[(first_folder_number, ast.parse(first_program))]]
    if len(programs) > 1:
        for i in range(1, len(programs)):
            folder_number, program = programs[i]
            current_skeleton = ast.parse(program)
            returned_index = find_index_of_similar_skeleton(
                bucket_skeletons, current_skeleton, threshold)
            if returned_index is not None:
                bucket_skeletons[returned_index].append(
                    (folder_number, current_skeleton))
            else:
                bucket_skeletons.append([(folder_number, current_skeleton)])

    return bucket_skeletons
