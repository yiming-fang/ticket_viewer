from request_tickets import *
import sys

sys.path.append("../")
from ticket_viewer.util import *
from ticket_viewer.request_tickets import *

zendesk = 'https://zcc978.zendesk.com'

def main():
    
    while True:
        print('\nSelect viewer option:')
        print('* Press 1 to view all tickets')
        print('* Press 2 to a ticket')
        print('* Type "quit" to exit')
        
        option = input()
        if option == 'quit':
            print('\nThanks for using the viewer. Goodbye.')
            break
        
        elif option == '1':
            list_url = f'{zendesk}/api/v2/tickets?per_page=25'
            print_list(list_url)
        
        elif option == '2':
            tid = input('Enter ticket number: ')
            print_single(tid)

if __name__ == "__main__":
    main()
