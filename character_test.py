from character import Character
harry = Character("Harry", "A smelly Wumpus")
harry.describe()

# Add some conversation for Harry when he is talked to
harry.set_conversation("Come closer. I can't see you!")

# Trigger a conversation with Harry
harry.talk()
# Set a weakness
harry.set_weakness("vegemite")

from character import Enemy
# Fight with harry
print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)