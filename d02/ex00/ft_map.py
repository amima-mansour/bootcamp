def ft_map(function_to_apply, list_of_inputs):
    for index, el in enumerate(list_of_inputs):
        list_of_inputs[index] = function_to_apply(el)
    return (list_of_inputs)
