
# 5 open answer question on history 
import time
#   import turtle
#   import winsound

#   wn = turtle.Screen()
#   wn.title("History QUIZ by DeAstisOFT")
#   wn.bgcolor("blue")
#   wn.setup(width=800, height=600)
#   wn.tracer(0)
def animation(text, delay=0.09):
    for char in text:
        print(char, end="", flush=True)  # No separator after the character
        time.sleep(delay)
    print("\n")
def load():
    print("\n")
    loadi="Loading..."
    animation(loadi)

def countdown(fromm, to=1, delay=0.8):
   for i in range(fromm, to - 1, -1):
    print(i, end="...", flush=True)
    time.sleep(delay)

# all input and aswer are lower cased to avoid any case sensitivity 

# CORE PART OF THE PROG 


intro = "Very weel. This is an open answer quiz, not case sensitive."
firstq = "You first question will appear shortly!".capitalize()
try_1 = "I don't think so! The right answer is:"
point = "Well done, next question!".capitalize()
final = "Correct, this was the last question. Your result is showing shortly! "



def again():
    retry= "Do you want to play again? "
    animation(retry)
    decision=input("(Y/N)").lower()
    if decision == "yes" or "y":
        y= "Ok, restarting..."
        animation(y)
        load()
    else:
        closing ="program closing".capitalize()
        animation(closing)
        countdown(3)
        print("\n")
        quit()
passed = "You passed, surprising..."
fail = "You Donkey! Disappointing..."
score = int(0)
        
#STARTING
while True:
    
    start ="Program is starting in:"
    for char in start:
            print(char, end="", flush=True)  # No separator after the character
            time.sleep(0.05)
    print("\n")    
    countdown(3)
    print("\n")

    starting="starting".capitalize()
    animation(starting)
    
    print("\n")


    welcome="Welcome to the History QUIZ!"
    animation(welcome)
    print("\n")
    start = input("are you ready to play? (y/n) ".capitalize()).lower()

    if start == "yes" or start == "y":
        load()
        print(intro)
    else:
        load()
        sure = input("are you sure? (y/n) ".capitalize()).lower()
        load()
        if sure == "yes" or sure == "y":
            print("ok, see you next time!".capitalize())
            quit()
        else:
            start1 = input("this means, you are ready to play? (y/n) ".capitalize()).lower()
            if start1 == "yes" or start1 == "y":
                load()
                print("alright, let's start!".capitalize())
                print("\n")
            else:
                print("ok, maybe next time!".capitalize())
                quit()
                
    load()
    animation(firstq)

    # QUESTIONS

        #QUESTION 1
    
    quest1 = input("The Great Wall of China is one of the most recognizable landmarks in the world. Which dynasty is credited with starting its construction? ").lower()
    answ1 = "Han Dynasty".lower() and "han".lower()
    if quest1.find(answ1) != -1:
        load()
    #    winsound.PlaySound(".\\bounce.wav", winsound.SND_ASYNC)
        print(point)
        score += 1
        load()
    else:
        print(try_1, answ1)
        print("DIOCANE")
        

        #QUESTION 2
    
    quest2 = input("The eruption of Mount Vesuvius in 79 AD buried which Roman cities? (Choose two) ").capitalize()
    queste2 = input("Second answer: ").capitalize()
    answ2 = ["Pompeii", "Ercolano"]
    if quest2 in answ2:
        score += 1
    else:
        print("")
    if queste2 in answ2:
        print(point) 
        score += 1
        load()
    else:
        print(f"{try_1} {answ2[0]} and {answ2[1]}")
        load()
        
        
        #QUESTION 3
    
    quest3 = input("The signing of which document formally ended the American Revolutionary War? ").lower()
    answ3 = "The Treaty of Paris" and "Treaty of Paris"
    if quest3 != answ3.lower():
        print(try_1, answ3)
        load()
    else:
        print(point)
        score += 1
        load()
        
        #QUESTION 4
    
    quest4 = input("Who led the Russian Revolution and established the world's first communist state? ").lower()
    answ4 = "Vladimir Lenin".lower()
    answe4 = "Lenin".lower()
    if quest4 != answ4 and quest4 != answe4:
        print(try_1, answ4)
        load()
    else:
        print(point)
        score += 1
        load()

        #QUESTION 5
    
    quest5 = input("The Rosetta Stone was a key to deciphering which ancient language? ").lower()
    answ5 = "Hieroglyphics".lower()
    if quest5 != answ5:
        print(try_1, answ5)
        load()
    else:
        score += 1
        print(final)
        load()
    
    
    time.sleep(0.2)
    print()
    lo= "Let's see how you did..."
    animation(lo)
    if score > 4:
        good=(f"{passed} your score is {score}")
        animation(good)
        again()
        continue
    else:
        bed=(f"{fail} your score is {score}")
        animation(bed), again()
        continue