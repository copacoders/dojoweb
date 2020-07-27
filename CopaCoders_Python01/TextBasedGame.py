""" Welcome to your First Python Project: Text Based Adventure Game"""

# To start, we are going to create an answer variable that will hold the players answers throughout the game
answer = input("Welcome to My Adventure Game! Would you like to play? (yes / no)\n").lower().strip()
# the reason we are using lower() and split() here is to make sure that the player's input matches our expected input 
# by making the input lowercase and removing spaces.

# Now it is time for our first IF-ELIF-ELSE statement 

# Let's check if the player said yes
if answer == "yes":
    print("Let's Play!")

    # Now here is where your story starts, my story will be about encountering a 50ft dragon. 
    # Let's tell the user the first decision they need to make and prompt them for an answer
    answer = input("You and your best friend Kyle, are walking in a dark and misty forest. As you walk, you come to a point where the trail breaks into two and you have to decide which direction to go. Do you go left or right? (left /right)\n").lower().strip()

    # We just asked the player to make another decision so now we need to check what they chose
    if answer == "left":
        print("You chose to go to the left, and as you turn, you see that the path has closed behind you. Strange, but you keep walking.")
        answer = input("Kyle sees a sign up ahead saying \"Stone of Victory -> this way\". You feel like something is not right about it, but you couldn't say what. Do you follow the sign? (yes / no)\n").lower().strip()

        if answer == "yes":
            print("Bad idea, always trust your instinct! As you follow the sign, you seem to get impossibly sleepy. You can't even keep your eyes open. You and Kyle see a nice patch of grass up ahead and decide to lie down. Except the patch of grass isn't grass and instead you are now falling. I guess you are on another adventure now... Game over")

        # I'm going to show you how to use an elif statement here as a guide 
        # but remember if you don't care about other answers that yes (any other answer means no), 
        # then you can use an else instead
        elif answer == "no":
            print("You're a natural, good job sticking with your instincts. You and Kyle keep traveling the way you were and eventually come across a castle. But what is that you hear? A dragon?")
            answer = input("Do you continue inside to find the stone? (yes / no)\n").lower().strip()


            # ***************************************************************************************************************************************
            # TODO: Alright this is where the story is left to you... Feel free to create your own story or continue mine. Best of luck, Adventurer!
            # ***************************************************************************************************************************************





    else:
        # Here we are assuming that if they didn't choose left, then they will be choosing right. 
        # This lessens the need for complexity as you don't need to handle a wrong response
        print("You turn to the right, and are hit with a wind so powerful it could pick up a tree. You continue forward looking for a place to stop. You see a small cave on your left and decide to wait out the wind.")
        answer = input("When you get to the cave, you realize Kyle is nowhere to be seen. YOu want to head back, but you know that won't help. You must continue on to find the stone of victory. Do you wait out the storm? (yes / no)\n").lower().split()

        # ***************************************************************************************************************************************
        # TODO: CREATE ANOTHER PATH - Do they make it to the stone, what do they face along the way? You decide! 
        # ***************************************************************************************************************************************

# Don't forget that we need to check if the play chose not to play the game 
# Any value that is not yes is considered as a no and thus we can use an else here
else:
    print("Maybe next time, it's really cool you know, you are certainly missing out. Anyways, see you later!")