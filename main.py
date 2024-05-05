# 1. flatten_dic

def flatten_dict(parent_dict):
    
    new_dict = {}
    
    def sep_key_value(child_dict):
        return child_dict

    for parent_key, parent_value in parent_dict.items():
        if type(parent_value) == dict:
            child_dict =sep_key_value(parent_value)
            for child_key, child_value in child_dict.items():
                new_key = parent_key + '.' + child_key
                new_dict[new_key] = child_value
        else:
            new_dict[parent_key] = parent_value

    print(new_dict)



flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})
#output: {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}


# 2.unflatten_dict

def unflatten_dict(parent_dict):




unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4})
#output:{'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}