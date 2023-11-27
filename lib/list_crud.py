def create_an_empty_list():
    return []

def create_a_list():
    return ["oranges", "kiwi", "bananas", "mangoes"]

def add_element_to_end_of_list(my_list, element):
    new_list = my_list.copy()
    new_list.append(element)
    return new_list



    

    

def add_element_to_start_of_list(my_list, element):
    new_list = my_list.copy()
    new_list.insert(0, element)
    return new_list


def remove_element_from_end_of_list(my_list):
    my_list.pop()
    return my_list



def remove_element_from_start_of_list(my_list):
    my_list[:] = my_list[1:]
    return my_list



def retrieve_first_element_from_list(my_list):
   
    if my_list:
        return my_list[0]
    else:
        return None  

def retrieve_element_from_index(my_list, index):
    
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return None  


def retrieve_last_element_from_list(my_list):
    
    if my_list:
        return my_list[-1]
    else:
        return None  

