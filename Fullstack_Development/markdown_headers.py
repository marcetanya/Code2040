#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:46:32 2019

@author: tanyallanas
"""

from collections import OrderedDict

headers = [('###### ', 6), ('##### ', 5), ('#### ', 4), ('### ', 3),
            ('## ', 2), ('# ', 1)]
headers_dict = OrderedDict(headers)

def recognize_headers(clean_markdown):
    """Identifies the header in the given string"""
    for key, value in headers_dict.items():

        if key in clean_markdown:
            return value


def markdownparser(markdown):
    """Takes in an HTML string and spits out markdown"""
    intermediary = markdown.strip()
    header = recognize_headers(intermediary)

    if header is None:
        return markdown

    length_header = header + 1
    header_check = intermediary[:length_header]
    actual_header = '#'*header + ' '
    
    if actual_header != header_check:
        return markdown

    else:
        index = header
        new_markdown = intermediary[index:].strip()

        return '<h{0}>{1}</h{0}>'.format(header, new_markdown)
