print("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
print("You are now on my island")
print("There are two doors in front of you. 🚪 a red door and 🚪 a blue door")

door = input("Which door do you want to open? ").lower()

if door == "blue":
    print("Great!🌟🌟🌟 Now you entered a room.")
    print("You found three boxes: 🎁 white, 🎁 black, 🎁 green")
    box = input("Which box do you open? ").lower()

    if box == "white":
        print("Winner!🏆🏆🏆 ...Yes You Win")

    elif box == "black":
        print("Oops! You opened a box filled with Snakes 🐍🐍🐍")

    elif box == "green":
        print("Oops! You opened a box filled with Crocodiles 🐊🐊🐊")
    
    else:
        print("Wrong choice!❌❌❌ Game Over.")

elif door == "red":
    print("Game Over!💥💥💥 You chose the wrong door.")

else:
    print("❌❌❌ You didnt choose red or blue!")
    