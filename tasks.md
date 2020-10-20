# TASKS
---

Todays tasks are all about READING CODE and making simple changes.

Here are the tasks for todays class.

1. Add three events

  - One of these events must make the player gain an item

  - The other event must make them use the item

  - The third event will make them loose the item without using it

  - I expect all students to be able to come up with something original
    i.e. no coping each other

  - HINT: Don't forget to add your new events to

  ```python
  self.events = [
      WrongTurn(),
      NormalTurn(),
      GoodTurn(),
      HealthTurn(),
      LuckTurn(),
      BestTurn(),
  ]
  ```

  In the `Game.__init__()` method.

2. Add two events

  - One event is has the possibility of an early VICTORY

  - The other event must have the possibility of an early GAME OVER

  - I expect all students to be able to come up with something original
    i.e. no coping each other

3. Change the `say` function in a way you feel improves the game.

  - Examples:

    - Add a ASCII box

    - Add some ASCII art

    - Use colours

    - Make the text add some player related info like
      panting when low on health

  - You may have to change the arguments to `say` if you do I
    recommend you make the new arguments optional and just use
    the new arguments in places you want.

  - Try and be imaginative

4. Make the game harder to win in some way

  - There are many ways too do this, examples:

    - Reduce chance of getting the right path

    - Reduce players health

    - Increase distance to the centre of the maze

    - Make more events where you can loose health/get closer to the minotaur

  - Don't go overboard it should still be playable

3. Make sure to fix all warning from flake8

4. Use python black to format your code
