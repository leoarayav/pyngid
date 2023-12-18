"""
The main class of the module.
"""

from .algorithm import Algorithm as algorithm
from .constants import PyNGIDConstants
from .id import Id

def go() -> Id:
  """
  Generate new identifier.
  
  Returns:
    Id: The generated identifier.
  """
  result = []
  for _ in range(PyNGIDConstants.IDENTIFIER_SECTION):
    result.append(algorithm.generate_section())
  return Id(
    '-'.join(result)
  )

def from_int(cls: any, id: Id) -> Id:
  """
  Convert integer to identifier.

  Parameters:
    id (int): identifier

  Returns:
    Id: The identifier.
  """
  if not isinstance(id, int):
    return None
  if id < 0:
    return None
  return cls.from_str(hex(id)[2:])

def from_str(cls: any, id: str) -> Id:
  """
  Convert string to identifier.

  Parameters:
    id (str): identifier
  
  Returns:
    Id: The identifier.
  """
  if not isinstance(id, str):
    return None
  if len(id) != PyNGIDConstants.IDENTIFIER_LENGTH:
    return None
  return cls(id)

def from_hex(cls: any, id: str) -> Id:
  """
  Convert hexadecimal string to identifier.

  Parameters:
    id (str): identifier
  
  Returns:
    Id: The identifier.
  """
  if not isinstance(id, str):
    return None
  if len(id) != PyNGIDConstants.IDENTIFIER_LENGTH:
    return None
  return cls.from_str(id)

def __wrapper(*args: any, **kwargs: any) -> Id:
  """
  Wrapper for the Id class.

  Parameters:
    *args (any): arguments
    **kwargs (any): keyword arguments
  
  Returns:
    Id: The identifier.
  """
  return Id(*args, **kwargs)