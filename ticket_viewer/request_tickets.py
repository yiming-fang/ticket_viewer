import requests
import sys

sys.path.append("../")
from ticket_viewer.util import *


credentials = 'yf2484@columbia.edu', 'Zendesk2021'
session = requests.Session()
session.auth = credentials
zendesk = 'https://zcc978.zendesk.com'


def print_list(list_url, test=False):
    response = session.get(list_url)
    error_handle(response)
    list_response = response.json()
    list_tickets = list_response['tickets']
    res = []

    print()
    for t in list_tickets:
        t_parse = parse_ticket(t)
        print(t_parse)
        if test:
            res.append(t_parse)
    print()
    
    next_page = list_response['next_page']
    prev_page = list_response['previous_page']
    if test:
        page = paginate(next_page, prev_page, test='M')
    else:
        page = paginate(next_page, prev_page)

    if page:
        print_list(page)
    return res


def print_single(tid):
    t_url = f'{zendesk}/api/v2/tickets/{str(tid)}'
    t_response = session.get(t_url)
    error_handle(t_response)
    t = t_response.json()['ticket']
    t_parse = parse_ticket(t)
    print(t_parse)
    return t_parse
