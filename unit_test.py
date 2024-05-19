

import unittest
from test_class import Player, Enemy  

class TestGame(unittest.TestCase):
    def test_player_creation(self):
        player = Player(180, 180)
        self.assertIsInstance(player, Player)

    def test_enemy_creation(self):
        enemy = Enemy(620, 160)
        self.assertIsInstance(enemy, Enemy)

if __name__ == '__main__':
    unittest.main()





