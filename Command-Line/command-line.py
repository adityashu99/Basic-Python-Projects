command = ""

cli_help = """
List of Commands :
--------------------
!help -> Prints the Help Page on Interface.
!quit -> CLoses the Command-Line.
!hello -> Print a simple Grreting Message.
"""

while(1):
    
    command = input("> ").lower()

    if command == "!hello":
        print("\nHello User, Greetings!\n")
    
    elif command == "!help" :
        print(cli_help)
    
    elif command == "!quit":
        break
    
    else :
        print("Invalid Command, Try Again.")
