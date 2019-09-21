import random


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
        strength = int(input("Enter the strength: "))
        return Weapon(name, strength)

    def create_armor(self):
        '''Prompt user for Armor information.
            return Armor with values from user input.
        '''
        name = input("Enter the name of your new armor: ")
        block = int(input("Enter the blocking power: "))
        return Armor(name, block)

    def create_hero(self):
        '''Prompt user for Hero information
            return Hero with values from user input.
        '''
        name = input("Enter a name for your new hero: ")
        new_hero = Hero(name)
        # loop for prompting abilities
        choice = "Y"
        while not (choice == "N" or choice == "n"):
            choice = input("Would you like to add a new ability (Y/N)?")
            if choice == "Y" or choice == "y":
                new_ability = self.create_ability()
                new_hero.add_ability(new_ability)
        # loop for prompting weapons
        choice = "Y"
        while not (choice == "N" or choice == "n"):
            choice = input("Would you like to add a new weapon (Y/N)?")
            if choice == "Y" or choice == "y":
                new_weapon = self.create_weapon()
                new_hero.add_ability(new_weapon)
        # loop for prompting armors
        choice = "Y"
        while not (choice == "N" or choice == "n"):
            choice = input("Would you like to add a new armor (Y/N)?")
            if choice == "Y" or choice == "y":
                new_armor = self.create_armor()
                new_hero.add_armor(new_armor)

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
            print("Result: no team wins!")

        # showing stats for first team
        print("Stats for Team One:")
        self.team_one.stats()
        print("These are the Heroes who are Still Alive on Team One:")
        for name in team_one_live_heroes_names:
            print(name)

        # showing stats for first team
        print("Stats for Team Two:")
        self.team_two.stats()
        print("These are the Heroes who are Still Alive on Team Two:")
        for name in team_two_live_heroes_names:
            print(name)


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()  # instanatiate Arena

    # Build teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
