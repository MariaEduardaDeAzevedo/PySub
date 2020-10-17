import sys
import functions

args = sys.argv

entry_len = len(args)
command = args[1]

if command == "init":
    try:
        if entry_len == 2:
            print("Hello! This is the PySub - Send version!\nConsult the README.md file to know how to send your submition.")
        elif args[2] == "to-config":
            functions.to_config()
        elif args[2] == "from-config":
            functions.from_config()
    except Exception as error:
        print(f"Something went wrong... {error}")

if command == "send":
    try:
        functions.send()
    except Exception as error:
        print(f"Something went wrong... {error}")

if command == "received":
    print('Ops... "received" is a Receive Version command')