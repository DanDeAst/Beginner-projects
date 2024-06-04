import random
import time

# Defs and variabls
tentative = 0
intro="Give me a range and guess which number I'm thinking! "
def a1():
    a_txt="The range's starts from... (insert a number) "
    for cha in a_txt:
            print(cha, end="", flush=True)
            time.sleep(0.07)
def b1():
    b_txt="Up to... (insert a number) "
    for cha in b_txt:
            print(cha, end="", flush=True)
            time.sleep(0.07)
    
def a_bigger_b():
    a_b = "The first number must be the smallest!"
    for cha in a_b:
            print(cha, end="", flush=True)
            time.sleep(0.07)

def loading():
    loadin = "Loading..."
    print("\n")
    for char in loadin:
        print(char, end="", flush=True)  
        time.sleep(0.1)
    print("\n")
    
def only_num():
    o_num="Only numbers ARE allowed!"
    for cha in o_num:
            print(cha, end="", flush=True)
            time.sleep(0.07)
    

    
# starting
loading()
for char in intro:
  print(char, end="", flush=True)  
  time.sleep(0.05)
loading()

#First loop (range numbers)
while True:
    try:
        a1()
        a = int(input(""))
        b1()
        b = int(input(""))
        if a >= b:
            a_bigger_b()
            continue
        
    except:
        only_num()
        loading()
        continue
    print(f"The number is between {a} and {b}")
    r = random.randint(a, b)
    print(r)
    try:
        guess = int(input("Guess the number: "))
    except:
        only_num()
        loading()
        continue

#Second loop (guessing)
    while guess != r:
        try:
            if guess < a or guess > b:
                inrange=(f"Your guess must be within the range from {a} to {b}.")
                for cha in inrange:
                    print(cha, end="", flush=True)
                    time.sleep(0.07)
                tentative += 1
                loading()
                guess = int(input("Guess the number: "))
                
            elif guess < r:
                below=(f"{guess} is below my number")
                for cha in below:
                    print(cha, end="", flush=True)
                    time.sleep(0.07)
                tentative += 1
                loading()        
                guess = int(input("Guess the number: "))
                
            elif guess > r:
                above=(f"{guess} is above my number")
                for cha in above:
                    print(cha, end="", flush=True)
                    time.sleep(0.07)
                tentative += 1
                loading()
                guess = int(input("Guess the number: "))  
                              
        except:
            only_num()
            loading()
            continue
    else:
        tentative += 1
        loading()
        well_done=(f"Well done, {guess} is correct. You guessed {tentative} times.")
        for cha in well_done:
                print(cha, end="", flush=True)
                time.sleep(0.07)
    print("\n")
    again1= "You won, would you like to try again? (Y/N)"
    for cha in again1:
            print(cha, end="", flush=True)
            time.sleep(0.07)
    again = input("").lower()
    if again == "y":
        s_over="ok another round!".capitalize()
        for cha in s_over:
            print(cha, end="", flush=True)
            time.sleep(0.07)
        loading()
        continue
    elif again == "n":
        bye=(f"See you soon! Goodbye!".capitalize())
        for cha in bye:
            print(cha, end="", flush=True)
            time.sleep(0.07)
        loading()
        exit()