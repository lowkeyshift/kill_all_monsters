import sys

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
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            if input ("Dodge? Y/N: ").lower() == 'y':
                if self.player.dodge():
                    print("You doged the attack!")
                else:
                    print("Couldn't dodge {} took a direct hit!".format(self.player))
                    self.player.hit_points -= 1
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
        else:
            print("{} isn't attacking this turn?!".format(self.monster))

    def player_turn(self):
        player_options = input("What will you do? [R]est, [A]ttack, [Q]uit: ").lower()
        if player_options == 'a':
            print("You're attacking {}!".format(self.monster))

            if self.player.attack:
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1

                    print("You hit {} with your {}!".format(self.monster, self.player.weapon))
            else:
                print("Your attacked failed.")
        elif player_options == 'r':
            self.player.rest()
        elif player_options == 'q':
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("Congradulations {}, you have defeated {}.".format(self.player,self.monster))
            self.monster = self.get_next_monster()


    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)

        if self.player.hit_points:
            print("You Win!")
        elif self.monsters or self.monster:
            print("You Were Eaten!!")
        sys.exit()

Game()