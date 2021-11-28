import unittest
from unittest import mock
from unittest import TestCase
import requests
import sys

sys.path.append("../")
from ticket_viewer.viewer import *
from ticket_viewer.request_tickets import *
from ticket_viewer.util import *

credentials = 'yf2484@columbia.edu', 'Zendesk2021'
session = requests.Session()
session.auth = credentials
zendesk = 'https://zcc978.zendesk.com'

class TicketViewerTests(TestCase):
    
    def test_parse(self):
        t_url = f'{zendesk}/api/v2/tickets/{1}'
        t_response = session.get(t_url).json()
        t = t_response['ticket']
        result = parse_ticket(t)
        expect = "Ticket with subject 'Sample ticket: Meet the ticket' opened by 1903665805947 on 2021-11-27 04:37"
        self.assertEqual(result, expect)

    def test_print_single(self):
        result = print_single(1)
        expect = "Ticket with subject 'Sample ticket: Meet the ticket' opened by 1903665805947 on 2021-11-27 04:37"
        self.assertEqual(result, expect)

    def test_print_list(self):
        result = len(print_list(f'{zendesk}/api/v2/tickets?per_page=25', test=True))
        expect = 25
        self.assertEqual(result, expect)

    def test_paginate_next(self):
        list_url = "https://zcc978.zendesk.com/api/v2/tickets.json?page=2&per_page=25"
        response = session.get(list_url)
        list_response = response.json()
        next_page = list_response['next_page']
        prev_page = list_response['previous_page']
        result = paginate(next_page, prev_page, test='N')
        expect = "https://zcc978.zendesk.com/api/v2/tickets.json?page=3&per_page=25"
        self.assertEqual(result, expect)

    def test_paginate_prev(self):
        list_url = "https://zcc978.zendesk.com/api/v2/tickets.json?page=2&per_page=25"
        response = session.get(list_url)
        list_response = response.json()
        next_page = list_response['next_page']
        prev_page = list_response['previous_page']
        result = paginate(next_page, prev_page, test='P')
        expect = "https://zcc978.zendesk.com/api/v2/tickets.json?page=1&per_page=25"
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()