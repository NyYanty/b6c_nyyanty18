import collections

y=(['c','a','a','a','b','b','b','b','b','b','c','c','c','c'])

def dict_count(y):
    return collections.Counter(y)

k = dict_count(y)
print(k)


