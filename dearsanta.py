#Project 3 -- Ayaka Ikawa, ITEC 6321 

#Title: Mad Libs "Dear Santa"
#Let's play Mad Libs for a total of 5 times before it ends!
#as Python automatically generates your story for you! Enter different words for each set.

loop = 1
list = ["You", "Are", "Done!"]

while(loop < 6): 

#user input
    name = input("Enter your name: ")
    numb = input("Enter a number: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    adj1 = input("Enter the adjective: ")
    adj2 = input("Enter the adjective: ")
    noun1 = input("Enter the noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    verb = input("Enter a verb in present tense: ")
    noun4 = input("Enter another noun: ")
    food1 = input("Enter a food: ")
    food1 = input("Enter a food: ")
    drink = input("Enter a drink: ")
    food2 = input("Enter a food: ")
    adj3 = input("Enter the adjective: ")

#print out Mad Lib story
    print(" ")
    print("Dear Santa Mad Lib:")
    print(" ")
    print("My name is " + name + " and I am " + numb + " years old. I live in " + city + ", " + state + ".")
    print("1. If you think I have been extra " + adj1 + " this year, I would like a " + adj2 + " " + noun1 +" ,under the tree, addressed to me." )
    print("2. It would make me even happier if you could put a " + noun2 + "inside of my stocking")
    print("3. I would also like to get a " + noun3 + " that can be " + verb + ".")
    print("4. When you come down the " + noun4 + " at my house on Christmas Eve, we will have " + food1 + "and" + drink + " waiting for you! I hope you like them!")
    print("5. We will leave out some " + food2 + " for the reindeer, too.")
    print("6. I hope you have a " + adj3 + " flight!")
    print(" ")

#user can replay the game 4 more times
    loop = loop + 1
    if loop > 5:
        print(list[0])
        print(list[1])
        print(list[2])

#print out "you are done!" to end the game. 