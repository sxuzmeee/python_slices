#1
# lst = [None, None, 1, [], (), {}, None]
#
# def de_none(lst):
#     new_lst = []
#     for item in lst:
#         if item is not None:
#             new_lst.append(item)
#     return new_lst
# print(de_none(lst))

#2

# ref_list = [0, 1, 2, 3, 4, 5]
# start = 4
# num = 40
# rep = 2
# def list_insert(ref_list, start, num, rep):
#
#     if len(ref_list) < start:
#         return -1
#     return ref_list[0:4] + [num] * rep + ref_list[start:]
# print(list_insert(ref_list, start, num, rep))

#3

# d = {'a': 1, 'b': None, 'c': [1, 2]}
# print(d)
# k = str(input())
# def get_elem(d, k):
#
#     if k in d:
#         return d[k]
#         print(d[k])
#     else:
#         print(d)
# print(get_elem(d, k))