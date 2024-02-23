def transposed(list_of_lists):
    from itertools import zip_longest

    tranposed_tuples = zip_longest(*list_of_lists, fillvalue=None)
    transposed_tuples_list = list(tranposed_tuples)

    transposed = [list(sublist) for sublist in transposed_tuples_list]

    return transposed
