def calculate_structure_sum(*args):
    all_sum = 0
    for i in args:
        if isinstance(i, (int, float, complex)):
            all_sum += i
            continue
        if isinstance(i, str):
            all_sum += len(i)
            continue
        elif isinstance(i, (list, set, tuple)):
            all_sum += calculate_structure_sum(*i)
        if isinstance(i, dict):
            all_sum += calculate_structure_sum(*i.items())

    return all_sum



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)