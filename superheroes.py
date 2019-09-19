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

        def add_ability(self, ability):
            """
            Parameters:
            ability (Ability)
            """
            self.abilities.append(ability)

        def attack(self):
            """
            Parameters: none
            """
            pass

        def defend(self, incoming_damage):
            """
            Parameters:
            incoming_damage (Integer)
            """

        def take_damage(self, damage):
            """
            Parameters:
            damage (Integer?)
            """
            pass

        def is_alive(self):
            """
            Parameters: none
            """
            pass

        def fight(self, opponent):
            """
            Parameters:
            opponent (Hero)
            """
            pass


if __name__ == "__main__":
    # testing Ability class
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    # testing Hero class
    my_hero = Hero("Alan Turing", 200)
    print(my_hero.name)
    print(my_hero.current_health)
