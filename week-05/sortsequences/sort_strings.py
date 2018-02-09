from datastubs import STRING_LIST

 
        
def reverse_alpha():
    """
    return the list of strings sorted in
    reverse alphabetical order.
    """

    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
    return the list of strings sorted in
    alphabetical order, but without regard to
    capitalization
    """
    return sorted(STRING_LIST, key=str.swapcase)



def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    def length(x):
        return len(x)
    return sorted(STRING_LIST, key=length)


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)
    """
    filter = [x for x in STRING_LIST if x.isdigit()]
    return sorted(filter)
    


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    """
    filter = [x for x in STRING_LIST if x.isdigit()]
    return sorted(filter, key=int)

