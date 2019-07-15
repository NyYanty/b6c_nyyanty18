def list_sort_str(ls):
    return sorted(list([x for x in ls if isinstance(x, str) and x.isalpha()]))


list = list_sort_str(['abc', 'def', -1, 2, 3, '-123', '888', 'hello'])
print(list)
