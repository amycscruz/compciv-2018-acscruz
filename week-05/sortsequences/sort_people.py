from datastubs import PEOPLE_LIST

def eval(x):
    country=x['country']
    age=x['age']
    return (country, age)
print (sorted(PEOPLE_LIST, key=eval))

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    def age(x):
        return x['age']
    return sorted(PEOPLE_LIST, key=age)

def oldest():
    """
    sort by age in descending order
    """
    def age(x):
        return x['age']
    return sorted(PEOPLE_LIST, key=age, reverse=True)

def name_reverse_alpha():
    def name(x):
        return x['name']
    return sorted(PEOPLE_LIST, key=name, reverse=True)

def country_then_age():
    def eval(x):
        country=x['country']
        age=x['age']
        return (country, age)
    return sorted(PEOPLE_LIST, key=eval)
