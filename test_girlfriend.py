import unittest
from girlfriend import GirlFriend


class GirlFriendTest(unittest.TestCase):

    def test_lookup_by_name(self):
        girl = GirlFriend()
        girl.add(name='Tricia', age=25, status='ex')
        girlfriend = girl.lookup(name='Tricia')
        self.assertEqual({'name': 'Tricia', 'age': 25, 'status': 'ex'}, girlfriend)
