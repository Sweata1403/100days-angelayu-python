import time
import sys

def loading_animation(message="Loading", duration=3):
    print(message, end="")
    for _ in range(duration):
        for dot in ". . .".split():
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(0.5)
        print("\r" + " " * (len(message) + 10), end="\r")
        print(message, end="")

# Start of the game
print(r'''
 _    _                          _     _             
| |  | |                        | |   (_)            
| |__| | __ _ _ __ ___   ___    | |__  _ _ __   __ _ 
|  __  |/ _` | '_ ` _ \ / _ \   | '_ \| | '_ \ / _` |
| |  | | (_| | | | | | |  __/   | | | | | | | | (_| |
|_|  |_|\__,_|_| |_| |_|\___|   |_| |_|_|_| |_|\__, |
                                                __/ |
                                               |___/ 
''')
print("Welcome to **Hogwarts Treasure Quest**! 🧙‍♂️")
print("Your mission is to find the hidden magical artifact before Voldemort does!")

loading_animation("Preparing your magical journey")
time.sleep(1)
print("\n✨ You wake up in the Gryffindor common room. A mysterious scroll appears...")

# Level 1
task_1 = input('\nThe scroll reads: "Two secret passages lie ahead. One leads to the Forbidden Forest 🌲, the other to the Chamber of Secrets 🐍."\nWhich path will you choose? Type "forest" or "chamber": ').strip().lower()

loading_animation("Casting spell to open the passage")
time.sleep(1)

if task_1 == "forest":
    print("\n🌲 You enter the Forbidden Forest and meet Hagrid. He gives you a magical map!")
    
    # Level 2
    task_2 = input('\nThe map shows two locations: "Hogsmeade" 🏘️ and "Room of Requirement" 🪄.\nWhere will you go? Type "hogsmeade" or "room": ').strip().lower()
    loading_animation("Teleporting to your chosen location")
    time.sleep(1)

    if task_2 == "room":
        print("\n🪄 The Room of Requirement appears! Inside, you find a riddle on a floating parchment.")
        
        # Level 3
        task_3 = input('\nRiddle: "I speak without a mouth and hear without ears. I have no body, but I come alive with wind."\nType your answer: ').strip().lower()
        loading_animation("Checking your answer with Dumbledore")
        time.sleep(1)

        if "echo" in task_3:
            print("\n🎉 Correct! The room reveals a hidden staircase leading to the final chamber.")
            
            # Final Level
            task_4 = input('\nYou face two magical doors: One glows red 🔴, the other blue 🔵.\nWhich door will you open? Type "red" or "blue": ').strip().lower()
            loading_animation("Unlocking the magical door")
            time.sleep(1)

            if task_4 == "blue":
                print("\n🏆 You found the legendary artifact: The Phoenix Feather of Eternity! Hogwarts is safe!")
                print(r'''
                 ___
                (o o)
        +----oOO--(_)-------+
        |  You are a true   |
        |  Hogwarts Hero!   |
        +------------------+
             |__|__|
              || ||
             ooO Ooo
                ''')
            else:
                print("\n💀 The red door was cursed! You are trapped in a time loop. Game Over.")
        else:
            print("\n💀 Wrong answer! The room collapses and you're sent back to the common room. Game Over.")
    else:
        print("\n💀 Death Eaters ambushed you in Hogsmeade. Game Over.")
else:
    print("\n💀 The Chamber of Secrets was a trap! You are petrified by the Basilisk. Game Over.")
