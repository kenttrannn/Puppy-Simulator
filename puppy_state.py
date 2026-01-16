#Kent Tran, Matthew Trinh
#Group 2
#December 3, 2025
#Puppy Simulator

from abc import ABC, abstractmethod

class PuppyState(ABC):
  @abstractmethod
  def play(self, puppy) -> str:
    """
    Abstract method for playing with the puppy
    """
    pass

  @abstractmethod
  def feed(self, puppy) -> str:
    """
    Abstract method for feeding the puppy
    """
    pass