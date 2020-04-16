class GirlFriend:

    def __init__(self):
        self.girlfriends = {}

    def add(self, **kwargs):
        self.girlfriends[kwargs['name']] = {'name': kwargs['name'], 'age': kwargs['age'], 'status': kwargs['status']}

    def lookup(self, name):
        return self.girlfriends[name]
