
def method_map(lst):
    
    return map(len, lst)

def length_of_word(lst):
    
    l = []
    for word in lst:
        l.append(len(word))
    return l


def method_list_comprehension(lst):
    
    l = [len(word) for word in lst]
