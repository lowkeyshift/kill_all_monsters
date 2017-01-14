from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:

    def setup(self):
        self.player = Character()
        self.monsters = [
           Goblin(),
           Troll(),
           Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monster.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # Check to see if the monster attacks
        # If so, tell the player
            # Check if the player wants to dodge
            #If so see if the dodge is successful
              # If it is , move on
            # If it's not, remove one player hit point
        # If the monster isn't attacking, tell the player too.

    def player_turn(self):
        #Let the player attack, rest, or quit
        #If they attack:
            # See if the attack is successful
                # If so, see if the monster dodges
                    # If dodged, print that
                    # If not dodged, subtract the right num of HP from the monster
                # If not a good attack, tell the player
            # If they rest:
                #Call the player.rest() method
            # If they quit, exit the Game
            # If they pick anything else, re-run this method

    def cleanup(self):
        #If the monster has no more HP:
            #up the player's experience
            #print a message
            #Get a new monster
