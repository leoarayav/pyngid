"""
This module contains the Id class
"""

import typing
from .constants import PyNGIDConstants

class Id:
  """
  Class Id from pyngid which representate an identifier and his properties

  Attributes:
    id (str): identifier
  """

  def __init__(self, id: str) -> None:
    """
    Class Id constructor
    """
    self.id = id

  @property
  def id(self) -> str:
    """
    Property identifier
    """
    return self._id

  @id.setter
  def id(self, id: str) -> None:
    """
    Id setter
    """
    if not isinstance(id, str):
      raise TypeError("Id must be a string")
    self._id = id
  
  def __str__(self) -> str:
    """
    String representation of Id
    """
    return f"Id({self.id})"
  
  def __repr__(self) -> str:
    """
    Representation of Id
    """
    return self.__str__()
  
  def __eq__(self, other: object) -> bool:
    """
    Equal operator
    """
    if not isinstance(other, Id):
      return False
    return self.id == other.id
  
  def __ne__(self, __value: object) -> bool:
    """
    Not equal operator
    """
    return not self.__eq__(__value)