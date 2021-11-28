import requests
import sys


def paginate(next_page, prev_page, test=None):
    if next_page:
        print('* Press N to go to the next page')
    if prev_page:
        print('* Press P to go to the previous page')
    if next_page or prev_page:
        print('* Press M to go back to the main menu')
        if test is not None:
            option = test
        else:
            option = input()
    while next_page or prev_page:
        if option.lower() == 'n' and next_page:
            return next_page
        elif option.lower() == 'p' and prev_page:
            return prev_page
        elif option.lower() == 'm':
            return None
        else:
            option = input('The command you entered is invalid. Please re-enter: ')

def parse_ticket(t):
    sub = "'" + t['subject'] + "'"
    req = t['requester_id']
    dt = ' '.join(t['created_at'][:-4].split('T'))
    string = f"Ticket with subject {sub} opened by {req} on {dt}"
    return string

def error_handle(response):
    if not response.ok:
        raise Exception('API exception:' + str(response))