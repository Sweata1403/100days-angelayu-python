print(r'''                            _.--.
                        _.-'_:-'|| 
                    _.-'_.-::::'|| 
               _.-:'_.-::::::'  || 
             .'`-.-:::::::'     || 
            /.'`;|:::::::'      ||_ 
           ||   ||::::::'     _.;._'-._ 
           ||   ||:::::'  _.-!oo @.!-._'-. 
           \'.  ||:::::.-!()oo @!()@.-'_.| 
            '.'-;|:.-'.$@.$ ()$%-'o.'\U|| 
              `>'-.!@%()@'@_%-'_.-o _.|'|| 
               ||-._'-.@.-'_.-' _.-o  |'|| 
               ||=[ '-._.-\U/.-'    o |'|| 
               || '-.]=|| |'|      o  |'|| 
               ||      || |'|        _| '; 
                    || |'|    _.-'_.-' 
               |'-._   || |'|_.-'_.' 
            jgs '-._'-.|| |' `_.-' 
                    '-.||_/.-' 
''')

print("🏝️ Welcome to **Treasure Island**!")
print("Your mission is to find the hidden treasure and escape the wrath of the dragons! 🐉")

# Level 1
task_1 = input('\nYou are at a dungeon. Two doors lie ahead. One leads to safety, the other to doom.\nWhich door will you open? Type "1" or "2": ').strip()

if task_1 == "1":
    print("\n🎉 Congratulations! You escaped the filthy dragon. A step closer to your treasure.")
    
    # Level 2
    print("\n🔥 Level 2: The Dragon's Nursery")
    print("You must feed the dragon babies. One door has spicy chillies 🌶️, the other has meat 🍖.")
    task_2 = input('Which door will you open? Type "left" or "right": ').strip().lower()

    if task_2 == "right":
        print("\n✅ Great choice! The babies are happily munching on meat. No noise, no danger.")
        
        # Level 3
        print("\n🚪 Final Level: The Silent Path")
        print("You now face two paths. One leads to a noisy ocean 🌊, the other is a silent road 🛣️.")
        task_3 = input('Choose your path: Type "left" or "right": ').strip().lower()

        if task_3 == "right":
            print("\n🏆 Hurray! You have successfully escaped the dungeons and claimed the treasure!")
            print(r'''
        d8b        888                  d8b                 
        Y8P        888                  Y8P                 
                   888                                      
888  888888 .d8888b888888 .d88b. 888d888888 8888b. 88888b.  
888  888888d88P"   888   d88""88b888P"  888    "88b888 "88b 
Y88  88P888888     888   888  888888    888.d888888888  888 
Y8bd8P 888Y88b.   Y88b. Y88..88P888    888888  888888  888 
 Y88P  888 "Y8888P "Y888 "Y88P" 888    888"Y888888888  888 
''')
        else:
            print("\n💀 Oh no! You fell into the ocean. The splash alerted the dragon. Game Over!")
    else:
        print("\n💀 Spicy chillies! The babies cried and the dragon devoured you. Game Over!")
else:
    print("\n💀 Wrong door! The dragon saw you and roasted you alive. Game Over!")
