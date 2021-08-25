print()
print("*** Coffee Order Demo ***")
print()

keep_going = ""
while keep_going == "":

    want_coffee = input("Do you want coffee?" ).lower()
    if want_coffee != "yes":
        print()
        print("wrong answer, you allways want coffee")
        print()
        continue

    else:
        print()
        print("good choice")
        print()
        break
    
print()
print("end of program")
print()