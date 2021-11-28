# zendesk ticket viewer

First, navigate inside the folder containing this module.
To use this ticker viewer, open the terminal and run the following command:
```
python ticket_viewer/viewer.py
```

There are two modes: viewing all tickets or a single ticket, identified with an id.  The CLI interface describes the expected commands as follows.
```
Select viewer option:
* Press 1 to view all tickets
* Press 2 to a ticket
* Type "quit" to exit
```

In the mode for viewing all tickets, tickets are paginated into lists containing 25 records each.  After displaying one page, the program prompts the user to choose whether to view the next/previous page, or exiting to the main menu.
```
* Press N to go to the next page
* Press P to go to the previous page
* Press M to go back to the main menu
```
