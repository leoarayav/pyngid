"""
This module represents the algorithm of PyNGID uses to generate identifiers and more
"""

import random
import typing as tp
from .constants import PyNGIDConstants

class Algorithm:
  """
  Class Algorithm which contains all methods for generating identifiers
  """
  @staticmethod
  def rotate(bits: int, shift: int) -> tp.Tuple[int, int]:
    """
    Rotate bits to the left.

    Parameters:
      bits (int): bits to rotate
      shift (int): shift to rotate
    
    Returns:
      Tuple[int, int]: The rotated bits
    """
    return ((bits << shift) | (bits >> (32 - shift))) & 0xFFFFFFFF

  @staticmethod
  def modulate(bits: int) -> tp.Tuple[int, int]:
    """
    Modulate bits.

    Parameters:
      bits (int): bits to modulate
    
    Returns:
      Tuple[int, int]: The modulated bits
    """
    return ((bits >> 16) ^ bits) & 0xFFFF
    
  @staticmethod
  def encrypt(data: str) -> str:
    """
    Encrypt data using own algorithm.

    Parameters:
      data (str): data to encrypt
    
    Returns:
      str: The encrypted data
    """
    data = data.encode('utf-8')
    key = random.randint(0, 0xFFFFFFFF)
    result = bytearray(4)
    for i in range(0, len(data), 4):
      block = int.from_bytes(data[i:i + 4], 'little')
      block ^= key
      block = Algorithm.rotate(block, 13)
      block ^= key
      result += block.to_bytes(4, 'little')
      result += Algorithm.modulate(block).to_bytes(4, 'little')
    return result.hex()
  
  @staticmethod
  def decrypt(data: str) -> str:
    """
    Decrypt data using own algorithm.

    Parameters: 
      data (str): data to decrypt
    
    Returns:
      str: The decrypted data
    """
    data = bytearray.fromhex(data)
    key = random.randint(0, 0xFFFFFFFF)
    result = bytearray(4)
    for i in range(0, len(data), 4):
      block = int.from_bytes(data[i:i + 4], 'little')
      block ^= key
      block = Algorithm.rotate(block, 13)
      block ^= key
      result += block.to_bytes(4, 'little')
    return result.decode('utf-8')
  
  @staticmethod
  def generate_section() -> str:
    """
    Generate new section of identifier.

    Returns:
      str: The new section
    
    Raises:
      RuntimeError: If the section is not valid
    """
    result = None
    while result is None:
      integer = random.randint(0, 0xFFFFFFFF)
      result = hex(integer)[2:]
      Algorithm.encrypt(result)
      if len(result) != PyNGIDConstants.IDENTIFIER_SECTION_LENGTH:
        result = None
    return result