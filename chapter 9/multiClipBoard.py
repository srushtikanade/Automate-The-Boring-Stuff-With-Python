import shelve
import sys
import pyperclip

mcb_shelf = shelve.open('mcb')

# Save the clipboard contents to keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' saved successfully!')

# Delete keyword and associated content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
    print([sys.argv[2] + 'has been deleted'])

elif len(sys.argv) == 2 and sys.argv[1].lower() != 'delete_all':
    # List stored keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('List of all keywords copied to clipboard')
    # Load content associated with chosen keyword to the clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(sys.argv[1] + 'is loaded successfully')
    # Inform user that their input doesn't match a saved keyword
    else:
        print('That keyword doesn\'t exist - so nothing'
              'has been loaded to the clipboard')

# Clear all shelved entries
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'deleteAll':
    mcb_shelf.clear()
    print('All keywords and associated contents have been deleted')

mcb_shelf.close()

