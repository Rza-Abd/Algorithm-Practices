
# Generate Stack class for using in Towers
from typing import Generic, TypeVar, List
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)
    

# Define Towers as a Stack

num_disks: int = 3

tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

# Ddefine initially condition : Push three disks to tower A
for disk in range(1, num_disks + 1):
    tower_a.push(disk)

# Define the Tower of Hanoi function
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    """ Tihs is a function for solving the Tower of Hanoi problem.
    It moves n disks from begin to end using temp.
    It uses recursion to solve the problem.
    Args:
        begin (Stack[int]): This is the stack that contains the disks to be moved.
        end (Stack[int]): This is the stack that contains the disks that have been moved.
        temp (Stack[int]): This is the stack that contains the temporary disks.
        n (int): This is the number of disks to be moved.
    """
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

    