"""Lists defines simple list related operations"""

from __future__ import division

def get_first_item(li):
    """Return the first item from the list"""
    return li[0]

def get_last_item(li):
    """Return the last item from the list"""
    return li[-1]

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    return li[1:3]

def get_sum(li):
    """Return the sum of the list items"""
    return sum(li)
    """
    sum = 0
    for i in li:
        sum += i
    retrun sum
    """

def get_avg(li):
    """Returns the average of the list items"""
    return get_sum(li) / len(li)
