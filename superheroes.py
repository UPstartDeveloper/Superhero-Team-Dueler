# Classes for Superhero Game
class Ability:
    def __init__(self, name, max_damage):
        """
        Parameters:
        name (String)
        max_damage(Integer)
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Parameters: none
        """
        pass


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
        """
        Parameters: none
        """
        pass


class Hero:
    self.abilities = list()  # stores Ability instances

    def __init__(self, name, starting_health):
        """
        Parameters:
        name (String)
        starting _health (Integer)
        """
        self.name = name
        self.starting_health = starting_health

    def __init__(self, name):
        """
        Parameters:
        name (String)
        starting_health set to default value
        """
        self.name = name
        self.starting_health = 100

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
