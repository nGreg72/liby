from django import template
import re

register = template.Library()

# @register.filter
# def replaceMe1(value):
#     return value.replace('&nbsp;', '')
#
# @register.filter
# def replaceMe2(value):
#     return value.replace('&ndash;', '')
#
# @register.filter
# def replaceMe3(value):
#     return value.replace('&trade;', '')
#
# @register.filter
# def replaceMe4(value):
#     return value.replace('&mdash;', '')
#
# @register.filter
# def replaceMe5(value):
#     return value.replace('&quot;', '')\


# @register.filter
# def replaceAll(value):
#
#     list_of_shit = ['&nbsp', '&ndash', '&mdash', '&trade', '&quot']
#     for i in list_of_shit:
#         return value.replace(i, '')

'''
Replace a set of multiple sub strings with a new string in main string.
'''


def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return mainString


@register.filter
def replaceAll(text):

    corrected_string = replaceMultiple(text, ['&nbsp;', '&ndash;', '&mdash;', '&trade;',
                                              '&quot;', '&amp;', '&raquo;', '&laquo;', 'bull'], " ")

    return corrected_string
