def ft_filter(function_to_apply, list_of_inputs):
    result_list = []
    for el in list_of_inputs:
        if function_to_apply(el):
            result_list.append(el)
    return (result_list)