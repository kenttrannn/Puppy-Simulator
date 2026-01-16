#Kent Tran, Matthew Trinh
#Group 2
#December 3, 2025
#Puppy Simulator

from puppy_state import PuppyState

class StateAsleep(PuppyState):
  def play(self, puppy):
    """
    Return a string indicating that the puppy is asleep and won't play right now.
    """
    return "The puppy is asleep. It doesn't want to play right now."

  def feed(self, puppy):
    """
    Return a string indicating that the puppy woke up the the sound of the food and is now eating.
    """
    from state_eat import StateEat
    puppy.change_state(StateEat())
    puppy.reset()
    puppy.inc_feeds()
    return "The puppy wakes up and comes running to eat"