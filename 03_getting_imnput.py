#ask the user for their name
username = input("what is your name?")

#Ask the user for their favourite integer
fav_num = int(input("Favourite Number?"))

#Double, half and sqaure the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
#greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
#Output the results of doubling,halving 
#and squaring their favourtite number
print("double is {} is {}".format(fav_num, double))
print("half is {} is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()