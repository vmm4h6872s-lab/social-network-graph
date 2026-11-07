class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends and friend is not self:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} is already in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
        if person1_name == person2_name:
            print("Friendship not created. A person cannot friend themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names) if friend_names else 'Nobody yet'}")


if __name__ == "__main__":
    network = SocialNetwork()

    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    network.add_person("Alex")  # Test duplicate person

    friendships = [
        ("Alex", "Jordan"),
        ("Alex", "Morgan"),
        ("Jordan", "Taylor"),
        ("Morgan", "Casey"),
        ("Taylor", "Riley"),
        ("Casey", "Riley"),
        ("Morgan", "Riley"),
        ("Alex", "Taylor"),
    ]
    for person1, person2 in friendships:
        network.add_friendship(person1, person2)

    network.add_friendship("Jordan", "Johnny")  # Test missing person
    network.add_friendship("Alex", "Jordan")  # Test duplicate friendship

    print("\nSocial Network:")
    network.print_network()
