"""
The Minotaur game.

Usage:
    minotaur.py
"""

import time
import random


class Player:
    """This class holds all the data on the player."""

    def __init__(self):
        """Create the player by setting up the variables."""
        self.distance_to_minotaur = 3
        self.distance_to_center = 3
        self.inventory = {}
        self.health = 100

    def has_item(self, item):
        """Check if the player has an item."""
        item_count = self.inventory.get(item, 0)
        if item_count > 0:
            return True
        else:
            return False

    def add_item(self, item):
        """Add an item to the players inventory."""
        item_count = self.inventory.get(item, 0)
        self.inventory[item] = item_count + 1

    def remove_item(self, item):
        """Remove an item from the players inventory."""
        if self.has_item(item):
            item_count = self.inventory.get(item, 0)
            self.inventory[item] = item_count - 1

    def get_damaged(self, amount):
        """Owww that hurt."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def get_healed(self, amount):
        """Make me feel better."""
        self.health += amount
        if self.health > 100:
            self.health = 100

    def move_closer_center(self):
        """Get closer to the money."""
        self.distance_to_center -= 1

    def gain_ground(self):
        """Run away from the minotaur."""
        self.distance_to_minotaur += 1

    def loose_ground(self):
        """Let the minotaur catch up, coz I am buff."""
        self.distance_to_minotaur -= 1


class Event:
    """Base class for all events."""

    def __init__(self):
        """Init this by setting times occured to zero."""
        self.times_event_occured = 0

    def say(self, message):
        """
        Print a message to the player.

        We do this as a function so that we can add flavor like a delay.
        """
        time.sleep(1)
        print(message)

    def choose(self, options):
        """Give the player some choices."""
        while True:
            self.say("What will you do?")
            for idx, option in enumerate(options):
                self.say(f"{idx+1}: {option}")
            choice = input()
            for idx, option in enumerate(options):
                if choice == str(idx + 1) or choice.lower() == option.lower():
                    return option

    def enter(self, player):
        """Use this to run the event."""
        raise NotImplementedError


class Start(Event):
    """This is the start event."""

    def enter(self, player):
        """Give the player the start messages and then just CONTINUE."""
        self.times_event_occured += 1
        self.say(
            "For whatever reason you find yourself in the mystical maze "
            "of the Minotaur"
        )
        self.say(
            "Untold riches await if only you can get the the center "
            "before the Minotaur catches you"
        )
        return "CONTINUE"


class End(Event):
    """VICTORY or...."""

    def enter(self, player):
        """Tell the player that they..."""
        self.times_event_occured += 1
        self.say("You can hardly believe your eyes")
        self.say("Before you lies the golden gates")
        self.say("Beyond which treasure surly awaits")
        self.say(
            "Quickly before the Minotaur can catch up to you. You reach for"
            " the lock"
        )
        self.say(
            "Slowly almost majestically the gates swing open almost"
            " welcoming you inside"
        )
        self.say("You step through only to find....")
        return "VICTORY"


class Death(Event):
    r"""
    Bring out your dead.

    The town crier said, paint your door with a cross of red.

            __________
           |\ __  __ /|
           | \  ||  / |
           | |\ || /| |
           | |_\||/_| |
           |  __\/__()|
           | |  /\  | |
           | | /||\ | |
           | |/ || \| |
           | /  ||  \ |
           |/|__||__|\|
           |__________|
    """

    def enter(self, player):
        """When the burden is just too much."""
        self.times_event_occured += 1
        self.say(
            "You stagger along the path for a moment longer only to slump"
            " to the ground"
        )
        self.say(
            "Your wounds are too great and you fear that this is the end!"
        )
        self.say(
            "As the world grows dark around you. You can only reflect on"
            " the folly of greed"
        )
        return "GAME OVER"


class WrongTurn(Event):
    """Was this I supposed to go left."""

    def enter(self, player):
        """Let the minotaur get closer."""
        self.say("You run deeper into the maze only to come into a dead end")
        self.say(
            "You must turn back and you are sure that then Minotaur "
            "is getting closer"
        )
        self.say("It's chilling howl curdles your blood")
        player.loose_ground()
        self.times_event_occured += 1
        return "CONTINUE"


class NormalTurn(Event):
    """Just another day in the trenches."""

    def enter(self, player):
        """In this event nothing really happens."""
        self.say(
            "You run deeper into the maze but it all looks the same to you"
        )
        self.say(
            "All you can do is keep running while the roars of the "
            "Minotaur keep bellowing through the maze"
        )
        self.times_event_occured += 1
        return "CONTINUE"


class GoodTurn(Event):
    """Goodbye minotaur."""

    def enter(self, player):
        """Let the minotaur get further away."""
        self.say(
            "You run deeper into the maze and the sounds of the Minotaur grow "
            "quiter"
        )
        self.say("You can't stop now though as you must keep running")
        self.times_event_occured += 1
        player.gain_ground()
        return "CONTINUE"


class HealthTurn(Event):
    """Medkit."""

    def enter(self, player):
        """Heal yourself."""
        self.say("You run deeper into the maze only to come into a dead end")
        self.say(
            "You must turn back and you are sure that then Minotaur"
            " is getting closer"
        )
        self.say("It's chilling howl curdles your blood")
        self.say(
            "You notice that the walls are coated in healing herbs"
            " rubbing some into your wounds would restore your health"
        )
        self.say("Should you use them?")
        choice = self.choice(["yes", "no"])
        if choice == "yes":
            if player.health < 100:
                self.say(
                    "Before the minotaur can gain any more ground you"
                    " quickly dress your wounds"
                )
                player.get_healed(30)
            else:
                self.say(
                    "You apply the herbs but feel a little silly since"
                    " you are in perfect health"
                )
                self.say("Maybe you just like to smell flowery")
            player.loose_ground()
        else:
            self.say(
                "You decide to just keep running, your just buff like that."
            )
        self.times_event_occured += 1
        return "CONTINUE"


class LuckTurn(Event):
    """Get the all powerful RUSTY SWORD."""

    def enter(self, player):
        """Find the sword and awe at its power."""
        self.say(
            "You run deeper into the maze but it all looks the same to you"
        )
        self.say(
            "All you can do is keep running while the roars of the "
            "Minotaur keep bellowing through the cave"
        )
        self.say("You notice an old rusty sword on the ground")
        if not player.has_item("rusty sword"):
            self.say("It may come in handy so you pick it up.")
            player.add_item("rusty sword")
        else:
            self.say("You can't carry two though so you just leave it here")
        self.times_event_occured += 1
        return "CONTINUE"


class BestTurn(Event):
    """Almost smell the money."""

    def enter(self, player):
        """Get closer to your goal."""
        self.say(
            "You run deeper into the maze and feel certain that you "
            "have moved in the right direction"
        )
        self.say(
            "You can almost smell the treasure and the dreams of "
            "riches motivate you to move faster"
        )
        player.move_closer_center()
        self.times_event_occured += 1
        return "CONTINUE"


class Minotaur(Event):
    """
    This event handles everything minotaur.

    This includes aspects like minotaur related death, and the rust sword.
    """

    def enter(self, player):
        """Deal with the minotaur or feel the end."""
        self.times_event_occured += 1
        self.say("As you turn the corner a large hulking shape looms over you")
        self.say("The Minotaur has found you!")
        if player.has_item("rusty sword"):
            player.remove_item("rusty sword")
            self.say("Without even thinking you slash your rusty sword widly")
            self.say(
                "The sword lodges into the Minotaurs calf and it gives "
                "out a grunt of pain"
            )
            self.say("While it is distracted you quickly escape")
            distance_gained = random.randint(1, 3)
            if distance_gained == 1:
                self.say(
                    "Almost as soon as the Minotaur is out of sight you"
                    " hear its roar charging you once more"
                )
                player.gain_ground()
            elif distance_gained == 2:
                self.say(
                    "You must have wounded it more that you thought as it"
                    " is several minutes before you can hear its's roars"
                    " once more"
                )
                player.gain_ground()
                player.gain_ground()
            else:
                self.say(
                    "You must have really hurt it as you can no longer "
                    "hear the Minotaur in the distance"
                )
                player.gain_ground()
                player.gain_ground()
                player.gain_ground()
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say(
                    "The minotaur makes a mighty lunge at you and you "
                    "are thrown against the far wall"
                )
                self.say(
                    "While the minotaur recovers from it's lunge you "
                    "make your escape as best you can"
                )
                player.get_damaged(20)
                player.gain_ground()
                player.gain_ground()
            elif rand_event == 2:
                self.say(
                    "The minotaur swings at you with the back of its mighty "
                    "hand"
                )
                self.say(
                    "You duck under it's next attack and quickly make "
                    "your escape before it can do any more damage to you"
                )
                player.get_damaged(10)
                player.gain_ground()
            else:
                self.say("Today is not your lucky day!")
                self.say(
                    "The minotaur has pinned you against a wall and "
                    "you can feel the world go dark"
                )
                self.say(
                    "Dreams of riches fill your vision only to be taken"
                    " away from you"
                )
                return "GAME OVER"
        return "CONTINUE"


class Game(Event):
    """This is the actual game class."""

    def __init__(self):
        """Init by creating a list of all the events."""
        self.events = [
            WrongTurn(),
            NormalTurn(),
            GoodTurn(),
            HealthTurn(),
            LuckTurn(),
            BestTurn(),
        ]
        self.start = Start()
        self.end = End()

        self.minotaur = Minotaur()
        self.death = Death()

    def play(self):
        """Play the game."""
        # New player every time to reset health and inventory
        player = Player()

        events = self.events
        start = self.start
        end = self.end

        minotaur = self.minotaur
        death = self.death

        event_result = start.enter(player)
        while event_result == "CONTINUE":
            # Get a list of numbers
            # Each number represents a path
            paths = list(range(0, len(events)))
            # Shuffle the list
            random.shuffle(paths)
            # Get just three paths
            three_path = paths[0:3]

            # Time to choose
            self.say("You are confronted with a choice of paths")
            choice = self.choose(["Left", "Forward", "Right"])
            if choice == "Left":
                idx = three_path[0]
            elif choice == "Forward":
                idx = three_path[1]
            elif choice == "Right":
                idx = three_path[2]

            # Use the chosen number to get the path
            my_path = events[idx]

            # Run the chosen path
            # The result will tell us it we have won/lost or need to keep going
            event_result = my_path.enter(player)

            # Post events
            if player.health <= 0:
                event_result = death.enter(player)
            elif player.distance_to_minotaur <= 0:
                event_result = minotaur.enter(player)
            elif player.distance_to_center <= 0:
                event_result = end.enter(player)

            if event_result == "GAME OVER":
                self.say(
                    """
                =================
                You LOOSE, sorry!
                =================
                """
                )
            elif event_result == "VICTORY":
                self.say(
                    """
                ================
                Congratulations
                you have won!
                We hope you enjoyed
                MINOTAUR!
                aka A Jumped up
                Rock, Paper, Scissors
                ================
                """
                )

    def stats(self):
        """List some stats."""
        for event in self.events:
            event_type = type(event)
            # FYI: `__name__` is a special variable that always equals
            # class name
            event_name = event_type.__name__
            print(
                f"You run into {event_name}, {event.times_event_occured} "
                "time(s)"
            )


# Run the game
if __name__ == "__main__":
    game = Game()
    try:
        game.play()
    except KeyboardInterrupt:
        print("Game Cancelled")
    finally:
        game.stats()
