from cave import Cave

cavern = Cave("Cavern")
cavern.set_description( " A damp and dirty cave.")

grotto = Cave("Grotto")
grotto.set_description( " A small cave with ancient graffiti.")

dungeon = Cave("Dungeon")
dungeon.set_description( " A large cave with a rack")

dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")

current_cave = cavern
dead = False
while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">")
    current_cave = current_cave.move(command)
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy): 

            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Bravo, hero you won the fight!")
                current_cave.set_character(None)
