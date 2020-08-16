# Welcome to your First Python Project
You've learned the ropes of what a variable is, how can you print that you LOVE DINOSAUORS, and even how to take input from a user. Now it's time to put it to work! 

We can't wait to see all of the awesome things you'll come up with!
<br />
<br />
<br />


# Text-Based Adventure Game 
You are tasked with designing a one-of-a-kind, uniquely you adventure game! Think about the last book you read, your favorite video game, the show or movie you just can't get enough of, or even your last family vacation. This is your story to tell, and we are so excited to hear it! 

## **The `if` , `if-else`, `if-elif-else` statement**
Before you begin, we have one more python topic to go over, and that is the mighty IF, IF-ELSE, and IF-ELIF-ELSE statement! 

Whenever you make a decision  
>_Do I want to go to the park or go to the bowling alley?_  
If I go to the park, I will play soccer, otherwise I will bowl. 

you are actually taking part in an if else decision. 

It's possible that you could go to the park and go to the bowling alley on the same day. The way we would show this in programing languages would be with an `if` Statement
```
if I go to the Park:
    I will play soccer

if  I go to the bowling alley:
    I will bowl
```
If you can only do one or the other though, this decision now becomes an `if-else` statement

```
if I go to the Park:
    I will play soccer
else:
    I will bowl at the bowling alley
```

As you can see, we can leave out the else _I go to the bowling alley_ as we are assuming that there are only two options. You either are going to the park or you are going to the bowling alley. 

However, this is not always the case. What if a new option becomes available? In this case, we can use the `if-elif-else` statement to specifically call out multiple options. Consider the following 
```
if I go to the Park:
    I will play soccer
elif I go to the bowling alley:
    I will bowl 
else:
    What else can I do today? 
```

`if`, `if-else`, and `if-elif-else` statements are incredibly powerful as they let us make decisions and determine what the outcome will be based on the condition. This will be the main building block of your project! 

## **Time To Code**
Now that you know about if statements, it is time to get started on crafting your own adventure. 

In this project, you will use nested if else statements (if-else statement inside of an if or an else) to direct a player through an adventure that you created. You can copy the code file for this project using the following link: [Python 01 - TextBased Game Code](https://github.com/copacoders/copacoders/raw/gh-pages/python/01-TextBasedGame.py) 

### General Guidelines 
- Get Creative! This is your moment! This is your shot to make the game you always wish you could play, or the book you always wish you could read, or any number of things. 

- Try to go at least 3 nested if statements in. We will be giving you a template to show you what this would look like so that you can get started. You can build out a game that goes on for 30 minutes if you'd like, the more paths, the more fun to play. 

- If you need inspiration, you can certainly look around on the interwebs for test-based python games ( I recommmend looking for games/tutorials that are focused towards beginners )

### Run the Program 
If you are reading this you've probably finished your awesome adventure game and are now trying to play it! First of all, congratulations, that's so cool and I can't wait to play it some day. 

If you are using a Python IDE (coding environment), such as VS Code as suggested in the Python 0 Tutorial, you should see a green triangle hopefully at the top right corner of your screen. If you click that, that should run your program. 

However, there is always the good ole fashion command line if you'd rather use that. 

- If you are on a windows computer, you will want to open the Command Prompt from your start menu ( you can search for `cmd` in the search bar and it should show up). 
- On a MAC OS device, you want to open the terminal which you can find either in your applications folder or by using the finder application. 

You may already have a terminal app of your choice and feel free to use that instead. 

Now you need to navigate to the file path at which your program is saved. Mine is at Desktop/CopaCoders_Python01 so I would type in the command line
```
cd Desktop/CopaCoders_Python01
```
After this, you will want to run your program using the following command

```
python TextBasedGame.py
```
_Use python if you only have one python version on your machine. Otherwise use python# where you replace # with the base version_

Example:
- Python 2.x -> python2 
- Python 3.x -> python3


If you renamed your program file, please use that name instead. If you built everything correctly, you should see your game's start printed to the screen and you should be able to play it as any player would. 

If you see an error, take a look at what it says and go back to your code to troubleshoot. We all have troubleshooting days and you will get through it. 
