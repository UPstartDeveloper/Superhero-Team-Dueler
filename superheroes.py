import random


def divide():
    """Add a dashed line to separate output."""
    print("----------------------------------------")


# Classes for Superhero Game
class Ability:
    def __init__(self, name, attack_strength):
        """
        Parameters:
        name (String)
        max_damage(Integer)
        """
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        """
        Parameters: none

        Returns:
        An int between 0 and the maximum attack value.
        """
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        """
        Parameters:
        name (String)
        max_block(Integer)
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """Returns a random integer between 0 and max_block strength."""
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        """
        Parameters:
        name (String)
        starting _health (Integer)
        """
        self.abilities = list()  # stores Ability instances
        self.armors = list()  # stores Armor instances
        self.name = name
        self.starting_health = self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        """
        Add ability to abilities list.
        Parameters: ability (Ability)
        """
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
           armor: Armor object
        '''
        self.armors.append(armor)

    def attack(self):
        """Calculate the total damage from all ability attacks.
            return: total (Integer)
        """
        total = 0
        for ability in self.abilities:
            total = total + ability.attack()
        return total

    def defend(self):
        """
        Runs block method on each armor and returns sum of all block.
        Parameters: none
        Returns: total_defense (Integer)
        """
        total_defense = 0
        if not len(self.armors) == 0:
            for armor in self.armors:
                total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        """
        Updates current_health by adding to it the
        difference of damage and the defend() method.

        Parameters: damage (Integer)
        """
        change_in_health = self.defend() - damage
        self.current_health += change_in_health

    def is_alive(self):
        """Return True and False based on current_health."""
        return self.current_health >= 0

    def add_kill(self, num_kills):
        '''Update kill count.'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''Update death count.'''
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon (Weapon object) to self.abilities.'''
        self.abilities.append(weapon)

    def fight(self, opponent):
        """
        Parameters:
        opponent (Hero)
        """
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                # check after each exchange of attacks for who's still alive
                if self.is_alive() and not opponent.is_alive():
                    print(f"{self.name} won!")
                    # update kill/death stats
                    self.add_kill(1)
                    opponent.add_deaths(1)
                elif not self.is_alive() and opponent.is_alive():
                    print(f"{opponent.name} won!")
                    # update kill/death stats
                    self.add_deaths(1)
                    opponent.add_kill(1)

    def str_to_object(self, name, object_type):
        '''This helper function searches for an object of a certain type,
           and returns the object that matches the name.
           Parameter: name(str)
                      object_type(Ability, Weapon, Armor)
           Returns: type(object_type)
        '''
        # choose which of Hero's property lists to search
        if object_type == "Ability" or object_type == "Weapon":
            for ability in self.abilities:
                if name == ability.name:
                    return ability
        elif object_type == "Armor":
            for armor in self.armors:
                if name == armor.name:
                    return armor

    def capture_index(self, name, object_type):
        '''This function returns the index position where an
           Ability/Weapon/Armor object stored in in respective list.
        '''
        if object_type == "Ability" or object_type == "Weapon":
            for i in range(len(self.abilities)):
                if name == self.abilities[i].name:
                    return i
        elif object_type == "Armor":
            for i in range(len(self.armors)):
                if name == self.armors[i].name:
                    return i

    def provide_prompts(self, obj_type, plural):
        '''A helper method to provide prompts to use in edit methods.
           Params:
           obj_type (str): type of object being edited
           plural (str): the plural form of the noun corresponding w/ obj_type
           Returns: prompts (list): contains common prompts
                    used through edit_ methods in Hero class
        '''
        prompts = [f"Do you know the {plural} of this Hero (Y/N)? ",
                   f"Here are the {plural} available for this Hero:",
                   f"Which {obj_type} would you like to change? \n",
                   f"Enter the name here. Enter Q to finish: ",
                   f"{obj_type} not found. Please try again: ",
                   f"N = name of {obj_type} \n",
                   f"A = attack strength of {obj_type} \n",
                   f"D = Delete this {obj_type} \n",
                   f"{obj_type} has been removed!"]
        return prompts

    def edit_powers(self, power_type):
        '''Prompts user for information and adjusts self.abilites,
           or self.armors.
           Param: power_type (str): specifies if Ability, Weapon, or Armor
                  is being edited.
        '''
        # decides which prompts to show user
        prompts = list()  # stores prompt strings
        if power_type == "Ability":
            prompts = self.provide_prompts("Ability", "Abilities")
        elif power_type == "Weapon":
            prompts = self.provide_prompts("Weapon", "Weapons")
        elif power_type == "Armor":
            prompts = self.provide_prompts("Armor", "Armors")

        choice = input(prompts[0])
        if choice.lower() == "n":  # user doesn't know all abilities
            # print all abilities
            divide()
            print(prompts[1])
            list_to_change = list()  # stores self.abilities or self.armors
            if power_type == "Ability" or power_type == "Weapon":
                list_to_change = self.abilities
            elif power_type == "Armor":
                list_to_change = self.armors
            #  printing the powers in their respective list
            for power in list_to_change:
                if power_type == "Ability":
                    if type(power) == Ability:
                        print(power.name)
                elif power_type == "Weapon":
                    if type(power) == Weapon:
                        print(power.name)
                elif power_type == "Armor":
                    print(power.name)
            divide()

        choice = input(prompts[2] + prompts[3])
        while not choice.upper() == "Q":
            # check to make sure valid Ability/Armor entered
            names_of_powers = list()
            for power in list_to_change:
                names_of_powers.append(ability.name)
            while choice not in names_of_powers:
                choice = input(prompts[4])
            else:  # valid object entered
                index = self.capture_index(choice, power_type)
                current_obj = list_to_change[index]
                op_choice = input("What would you like to change? \n" +
                                  prompts[5] +
                                  prompts[6] +
                                  prompts[7] +
                                  "Please select one: ")
                if op_choice.upper() == "N":
                    new_name = input("Please enter a new name: ")
                    # replaces Ability object
                    new_obj = Ability(new_name, current_obj.max_damage)
                    list_to_change[index] = new_obj
                    assert new_name == list_to_change[index].name
                    divide()
                elif op_choice.upper() == "A":
                    new_stren = input("Enter a new attack strength: ")
                    list_to_change[index] = Ability(choice, new_stren)
                    err_msg = "Attack strength change failed!"
                    assert new_stren == list_to_change[index].max_damage, (
                            err_msg)
                    divide()
                elif op_choice.upper() == "D":
                    list_to_change.pop(index)
                    print(prompts[8])  # print removal message
                    divide()
                else:
                    print("Sorry, that choice is invalid.")


# a Hero that can steal Abilities or Armors from other heroes
class Thief(Hero):
    def steal(self, other_hero):
        '''A function to take an Ability, Weapon, or Armor from another Hero.
           Param: other_hero(Hero)
           Return: None
        '''
        if not len(other_hero.abilities) == 0:
            stolen = other_hero.abilities[0]
            other_hero.abilities.pop(0)
            self.abilities.append(stolen)
        elif not len(other_hero.armors) == 0:
            stolen = other_hero
        else:
            print(f"{self.hero} cannot steal from {other_hero.name}")


class Weapon(Ability):
    def attack(self):
        """ This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage // 2, self.max_damage)


class Team:
    def __init__(self, name):
        ''' Initialize a team with a team name.
            Parameter: name (str)
        '''
        self.name = name
        self.heroes = list()  # an empty list of heroes on the team

    def add_hero(self, hero):
        '''Add a new hero to the team.
           Parameter: hero (Hero obj)
        '''
        self.heroes.append(hero)

    def remove_hero(self, name):
        ''' Remove a hero from the team by their name.
            If the hero isn't found, return 0.
            Parameter: name (str)
        '''
        # check if the Hero is present
        hero_names = list()
        for hero in self.heroes:
            hero_names.append(hero.name)
        if name not in hero_names:
            return 0
        # removes a Hero
        else:
            for hero in self.heroes:
                if hero.name == name:
                    self.heroes.remove(hero)

    def view_all_heroes(self):
        '''List all heroes on the team.'''
        for hero in self.heroes:
            print(hero.name)

    # methods for teams to attack/defend
    def attack(self, other_team):
        '''Battle each team against one another.'''
        # Randomly selects a Hero from each team
        max_index = len(self.heroes) - 1  # last index position in heroes list
        hero = self.heroes[random.randint(0, max_index)]
        max_index = len(other_team.heroes) - 1
        enemy = other_team.heroes[random.randint(0, max_index)]

        # if the hero is a Thief, steal from the enemy before the fight
        if type(hero) == Thief:
            hero.steal(enemy)

        hero.fight(enemy)

    def revive_heroes(self, heath=100):
        '''Reset all heroes' health to starting_health.'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print stats of the team.'''
        print("Here are the kill/death ratios for your team's Heroes:")
        ratios = list()  # stores all ratios for the team
        for hero in self.heroes:
            if not hero.deaths == 0:
                ratio = hero.kills/hero.deaths
                ratios.append(ratio)
                print(f"{hero.name}: {ratio}")
            else:
                print(f"{hero.name}: No deaths, no ratio")

        # calculates and prints average kill/death ratio
        sum = 0
        for ratio in ratios:
            sum += ratio
        if not len(ratios) == 0:
            avg = sum/len(ratios)
            print(f"Average kill/death ratio: {avg}")
        else:
            print("Average kill/death ratio: N/A")

    def remove_all_heroes(self):
        '''A function to delete all heroes on a team.'''
        for hero in self.heroes:
            self.heroes.remove(hero)


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input.
        '''
        name = input("Enter the name for your new ability: ")
        strength = int(input("Enter the attack strength: "))
        return Ability(name, strength)

    def create_weapon(self):
        '''Prompt user for Weapon information.
            return Weapon with values from user input.
        '''
        name = input("Enter the name of the new weapon: ")
        strength = input("Enter the strength: ")
        return Weapon(name, int(strength))

    def create_armor(self):
        '''Prompt user for Armor information.
            return Armor with values from user input.
        '''
        name = input("Enter the name of your new armor: ")
        block = int(input("Enter the blocking power: "))
        return Armor(name, block)

    def prompt_for(self, hero, attribute):
        '''Helper function for create_hero(). Continually prompts user for
           abilities/weapons/armors for their new Hero.

           Parameter: attribute (str): whichever of the three Hero attributes
                      that the user is currently being prompted to give.
                      hero (Hero): object whose properties are being changed.
            Returns: nothing
        '''
        choice = ""
        while not (choice == "N" or choice == "n"):
            choice = input(f"Would you like to add a new {attribute} (Y/N)?")
            if (choice == "Y" or choice == "y") and attribute == "ability":
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif (choice == "Y" or choice == "y") and attribute == "weapon":
                new_weapon = self.create_weapon()
                hero.add_ability(new_weapon)
            elif (choice == "Y" or choice == "y") and attribute == "armor":
                new_armor = self.create_armor()
                hero.add_armor(new_armor)

    def prompt_all(self, hero):
        '''A function to go through prompt_for 3 times,
           one for adding Abilities, Weapons, and Armors to the Hero.
        '''
        # loop for prompting abilities
        self.prompt_for(hero, "ability")
        # loop for prompting weapons
        self.prompt_for(hero, "weapon")
        # loop for prompting armors
        self.prompt_for(hero, "armor")

    def create_hero(self):
        '''Prompt user for Hero information
            return Hero with values from user input.
        '''
        #  user can choose to make Hero a Thief
        make_thief = input("Is this Hero able to steal(Y/N)? ")
        if make_thief.lower() == "y":
            name = input("Enter a name for your new hero: ")
            new_hero = Thief(name)
            self.prompt_all(new_hero)
        else:
            name = input("Enter a name for your new hero: ")
            new_hero = Hero(name)
            self.prompt_all(new_hero)

        return new_hero

    def build_team_one(self):
        '''Prompt the user to build team_one.'''
        team_one_name = input("Enter name for Team One: ")
        self.team_one = Team(team_one_name)
        team_size = input("Enter the size of this team: ")

        '''
        for each hero requested by user,
        create a Hero object
        and append it to the heroes list in the Team object
        '''
        heroes_added = 0
        while heroes_added < int(team_size):
            new_team_player = self.create_hero()
            self.team_one.add_hero(new_team_player)
            heroes_added += 1

    def build_team_two(self):
        '''Prompt the user to build team_two.'''
        team_two_name = input("Enter the name for Team Two: ")
        self.team_two = Team(team_two_name)
        team_size = input("Enter the size of this team: ")

        '''
        for each hero requested by user,
        create a Hero object
        and append it to the heroes list in the Team object
        '''
        heroes_added = 0
        while heroes_added < int(team_size):
            new_team_player = self.create_hero()
            self.team_two.add_hero(new_team_player)
            heroes_added += 1

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statisitics to terminal.'''

        # lists to contain names of all alive heroes on teams
        team_one_live_heroes_names = list()
        team_two_live_heroes_names = list()

        # winning team decided by whom has more alive heroes
        live_one_heroes = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                live_one_heroes += 1
                team_one_live_heroes_names.append(hero.name)

        live_two_heroes = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                live_two_heroes += 1
                team_two_live_heroes_names.append(hero.name)

        # decides which team won
        if live_one_heroes > live_two_heroes:
            print("Result: Team One wins!")
        elif live_two_heroes > live_one_heroes:
            print("Result: Team Two wins!")
        else:
            print("Result: No Team wins!")

        # showing stats for first team
        print("Stats for Team One:")
        self.team_one.stats()
        print("These are the Heroes who are Still Alive on Team One:")
        divide()
        for name in team_one_live_heroes_names:
            print(name)
        divide()

        # showing stats for first team
        print("Stats for Team Two:")
        self.team_two.stats()
        print("These are the Heroes who are Still Alive on Team Two:")
        divide()
        for name in team_two_live_heroes_names:
            print(name)

    def recreate_teams(self):
        '''Removes all heroes from each team, and then rebuilds them.'''
        self.team_one.remove_all_heroes()
        self.team_two.remove_all_heroes()
        self.build_team_one()
        self.build_team_two()

    def edit_team(self, selected_team):
        '''Changes parts of the team which user selects.
           Param: selected_team (Team): Team being changed
        '''
        divide()
        see_heroes = input("View the heroes on this Team (Y/N)?")
        if see_heroes.lower() == "y":
            selected_team.view_all_heroes()
        divide()
        # check if the user enters a valid Hero
        hero_names = list()
        for hero in selected_team.heroes:
            hero_names.append(hero.name)
        num_changes = input("Enter the number of Heroes you'd like to change ")
        for i in num_changes:  # repeats for Hero user wants to change
            hero_choice = input(f"Enter Hero #{i} you'd like to change: ")
            while hero_choice not in hero_names:
                hero_choice = input("Name cannot be found. Please try again: ")
            print("Name found! Success!")
            # when the Hero is found, pull the Hero out of the Team's hero list
            # and store it in hero_choice
            for hero in selected_team.heroes:
                if hero_choice == hero.name:
                    hero_choice = hero  # changes from str to Hero type
            divide()
            attribute_choice = input("Which property is being changed? \n" +
                                     "A = hero's abilites \n" +
                                     "W = hero's weapons \n" +
                                     "AR = hero's armors \n" +
                                     "Please enter your choice: ")
            if attribute_choice == "A":
                hero_choice.edit_powers("Ability")
            elif attribute_choice == "W":
                hero_choice.edit_powers("Weapon")
            elif attribute_choice == "AR":
                hero_choice.edit_powers("Armor")


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()  # instanatiate Arena

    # Build teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
            # Ask user if they want to reset the teams
            reset_choice = input("Would you like to reset the teams (Y/N)?")
            if reset_choice.lower() == "y":
                arena.recreate_teams()
            elif reset_choice.upper() == "N":
                # Ask user if they want to change the teams
                edit_choice = input("Would you like to edit the teams (Y/N)? ")
                if edit_choice.lower() == "y":
                    team_choice = input("Enter the Team you want to edit: ")
                    if team_choice == arena.team_one.name:
                        arena.edit_team(arena.team_one)
                    elif team_choice == arena.team_two.name:
                        arena.edit_team(arena.team_two)
