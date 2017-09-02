"""Lists defines simple list related operations"""

def get_first_item(li):
    """Return the first item from the list"""
    li.index(0)

def get_last_item(li):
    """Return the last item from the list"""
    return li.index(-1)

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    return li.index[1:2]

def get_sum(li):
    """Return the sum of the list items"""
    sum = 0
    i = 0
    while i < len(li)
        sum += li.index(i)
    return sum
def get_avg(li):
    """Returns the average of the list items"""
    sum = get_sum(li)
    return sum/len(li)

