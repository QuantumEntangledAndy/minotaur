# TASKS
---

Todays tasks are all about READING CODE and making simple changes.

Here are the tasks for todays class.

Each event has the general form

```python
class EventName(Event):
  """Description of event."""

  def enter(self, player):
    """This part is run when the event starts."""
    self.say("Say something interesting")

```

You will need to create 3 new events of this form that are interesting.

1. a) Add three events

  - One of these events must make the player gain an item

    - Try reading: `class LuckTurn(Event)` to understand how I did it and make something similar.

  - The other event must make them use the item

  - The third event will make them loose the item without using it

  - I expect all students to be able to come up with something original
    i.e. no coping each other


1. b) After you have made the events:
  - Add your new events to this AFTER YOU HAVE MADE THEM

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

**POST** After you have made your events run this in the terminal (in the same directory as `minotaur.py`)

```bash
git add -A
git commit -m "New events added"
```


2. Change the `say` function in a way you feel improves the game.

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

**POST** After you have done this run this in the terminal (in the same directory as `minotaur.py`)

  ```bash
  git add -A
  git commit -m "Improved the say function"
  ```

3. Make the game harder to win in some way

  - There are many ways too do this, examples:

    - Reduce chance of getting the right path

    - Reduce players health

    - Increase distance to the centre of the maze

    - Make more events where you can loose health/get closer to the minotaur

  - Don't go overboard it should still be playable

**POST** After you have done this run this in the terminal (in the same directory as `minotaur.py`)

  ```bash
  git add -A
  git commit -m "Made the game harder to win"
  ```

4. Make sure to fix all warning from flake8 (the little red dots)

**POST** After you have done this run this in the terminal (in the same directory as `minotaur.py`)

  ```bash
  git add -A
  git commit -m "Applied flake8 style"
  ```

5. Use python black to format your code

```bash
black minotaur.py
```

**POST** After you have done this run this in the terminal (in the same directory as `minotaur.py`)

  ```bash
  git add -A
  git commit -m "Made it BLACK like my coffee"
  ```


6. DONE

**POST** After EVERYTHING run this

    ```bash
    git archive -o "minotaur.zip"
    ```

Upload this zip into jypyter hub in the folder

`appcompchem01(or 02)/06-Minotaur/`

Then click submit on the assignments tab
