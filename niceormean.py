# Python 2.7.12
# Author: Jacob Wally Jones
# Purpose: Drill for text based game...

#Always Forward; Forward Always.



def start(nice=0, mean=0, name=""):
#Gets the name of player
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
#Check if new game, if so get name. If not thank player for playing and continue.
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted by different people. You can be nice or mean to them.")
                    print("At the end of the game your fate will be influenced by what you do.")
                    stop = False
    return name
                    
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for conversation... \nWill you show kindness or not? y/n:").lower()
        if pick == "y":
            print("You greet them cordially and show them the respect they deserve. \nYou can tell this makes them feel good.")
            nice = (nice + 1)
            stop = False
        if pick == "n":
            print ("\nYou pretend to ignore the persons attempt to start a conversation. \nThe stranger storms off muttering something while looking over his shoulder.")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #passes the 3 variables to the score()

def show_score(nice,mean,name):
    print ("\n{}, You are currently ({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is passing the three values stored in the variables
    if nice >= 5:
        win(nice,mean,name)
    if mean >= 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nGood for you {}!, you are a nice person and have been recognized as such by your peers.".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nYou have performed selfishly {}, your peers have deemed you socially inept. \nWhether or not this will benefit you is yet to be seen".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to try again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you next time!")
            stop = False
            exit()
        else:
            print("\nY for Yes, or N for NO ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)
        
            


if __name__ == "__main__":
    start()
