# Author: Ben Mickens
# Due Date: 11-16-2025
# Function: This program implements the character tracker class

import character_tracker_utils as ct

def main():

    # Create 2 characters
    character1 = ct.GameCharacter("Mario", "Warrior", 100, 50)
    character2 = ct.GameCharacter("Luigi", "Mage", 100, 50)

    # Display the character's initial stats
    print("\n--- Character stats ---")
    character1.display_info()
    character2.display_info()

    # Have one character gain 50 XP, level up, and display their updated stats
    character1.gain_xp(50)
    character1.level_up()

    print(f"\n{character1.name} slayed the dragon, gained 50 XP, and leveled up!")
    print(f"\n{character1.name}'s updated stats:")
    character1.display_info()

# Run the program
if __name__ == "__main__":
    main()