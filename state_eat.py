#Kent Tran, Matthew Trinh
#Group 2
#December 3, 2025
#Puppy Simulator

from puppy_state import PuppyState

class StateEat(PuppyState):
  def play(self, puppy):
    """
    The puppy will stop eating and start playing.
    """
    from state_play import StatePlay
    puppy.change_state(StatePlay())
    puppy.reset()
    puppy.inc_plays()
    return "The puppy looks up from it's food and chases after the ball you threw."

  def feed(self, puppy):
    """
    Adds food to the puppy's bowl, after 3 times of feeding, the puppy will fall asleep.
    """
    puppy.inc_feeds()
    result = "The puppy continues to eat as you add another scoop of kibble to the bowl."

    if puppy.feeds >= 3:
      from state_asleep import StateAsleep
      puppy.change_state(StateAsleep())
      puppy.reset()
      result += "\nThe puppy ate so much it fell asleep."
    
    return result