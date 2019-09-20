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
            total += ability.attack()
        return total

    def defend(self, incoming_damage):
        """
        Runs block method on each armor and returns sum of all block.
        Parameters: incoming_damage (Integer)
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
        change_in_health = damage - self.defend(damage)
        self.current_health -= change_in_health

    def is_alive(self):
        """Return True and False based on current_health."""
        return self.current_health >= 0

    def fight(self, opponent):
        """
        Parameters:
        opponent (Hero)
        """
        if len(self.abilities) and len(opponent.abilities) == 0:
            print("Draw!")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                # check after each exchange of attacks for who's still alive
                if self.is_alive() and not opponent.is_alive():
                    print(f"{self.name} won!")
                    self.add_kill()
                    opponent.deaths += 1
                elif not self.is_alive() and opponent.is_alive():
                    print(f"{opponent.name} won!")
                    self.deaths += 1
                    opponent.add_kill()

    def add_kill(self, num_kills):
        '''Update kill count.'''
        self.kill += num_kills


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


if __name__ == "__main__":
    '''
    # testing code
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    '''
    '''
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    '''
    '''
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
    '''
    '''
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    '''

    '''
    Previous tests
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    # testing Hero class
    my_hero = Hero("Alan Turing", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    another_ability = Ability("Great Debugging", 50)
    my_hero.add_ability(ability)
    my_hero.add_ability(another_ability)
    print(my_hero.abilities)
    '''
