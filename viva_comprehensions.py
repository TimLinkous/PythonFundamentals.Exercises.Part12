from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:

   """
    generate a list of integers from start to stop that match the parity condition

    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: starting integer
    :param stop: ending integer
    :param parity: parity condition match (odd or even)
    :return: a list of integers matching the parity condition
    """
   
   if parity == Parity.ODD:
      return [i for i in range(start, stop) if i % 2 != 0] # return odd numbers
   elif parity == Parity.EVEN:
      return [i for i in range(start, stop) if i % 2 == 0] # return even numbers
    #pass


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:

    """
    create a dictionary where the keys are the numbers from start to stop (inclusive) and the values are
    the squared values of the keys

    

    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start: starting integer
    :param stop: ending integer
    :param strategy: stragegy, which is a callable object (function or lambda)
    :return: return a dictionary where keys are the numbers from start to stop and the values are based on the strategy function
    """
    return {i: strategy(i) for i in range(start, stop)} 
    #constructs a dictionary with i as the key and strategy(i) as the value
    #pass


def gen_set(val_in: str) -> Set[str]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in: input string
    :return: A set of unique characters (lowercase) from the input string.
    """
    return {char.upper() for char in val_in if char.islower()} # returns a set of unique characters from the input string
    #returns set where characters are converted to lowercase in the input string
    #pass
