#Kent Tran, Matthew Trinh
#Group 2
#December 3, 2025
#Puppy Simulator

from puppy_state import PuppyState

class StatePlay(PuppyState):
  def play(self, puppy):
    """
    Puppy is already playing. Continues playing with the puppy, puppy falls asleep after 3 times of playing.
    Returns a string describing the puppy's current state.
    """
    puppy.inc_plays()
    result = "You throw the ball again and the puppy excitedly chases it."

    if puppy.plays >= 3:
      from state_asleep import StateAsleep
      puppy.change_state(StateAsleep())
      puppy.reset()
      result += "\nThe puppy played so much it fell asleep."

    return result

  def feed(self, puppy):
    """
    Puppy will ignore food while playing.
    Returns a string indicating that the puppy is too busy playing with the ball right now.
    """
    return "The puppy is too busy playing with the ball right now."