def ft_reduce(function_to_apply, list_of_inputs):
    tmp = None
    for el in list_of_inputs:
        if tmp is None:
            tmp = el
            continue
        tmp = function_to_apply(tmp, el)
    return tmp