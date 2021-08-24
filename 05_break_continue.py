print()
print("*** Looping Demo #2 ***")
print()

for item in range(0,5):
    print(item)

    #ask user if they want to keep going
    keep_going = input("<enter> to keep looping or any key to quit")

    #h
    if keep_going != "":
        break
    
print()
print("we are done")
print()