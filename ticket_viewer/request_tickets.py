import requests
from util import *

credentials = 'yf2484@columbia.edu', 'Zendesk2021'
session = requests.Session()
session.auth = credentials
zendesk = 'https://zcc978.zendesk.com'


def print_list(list_url):
    response = session.get(list_url)
    error_handle(response)
    list_response = response.json()
    list_tickets = list_response['tickets']
    
    print()
    for t in list_tickets:
        parse_ticket(t)
    print()
    
    next_page = list_response['next_page']
    prev_page = list_response['previous_page']
    paginate(next_page, prev_page)

def print_single(tid):
    t_url = f'{zendesk}/api/v2/tickets/{str(tid)}'
    t_response = session.get(t_url)
    error_handle(t_response)
    t = t_response.json()['ticket']
    parse_ticket(t)