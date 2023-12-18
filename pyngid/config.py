"""
This module contains the configuration for pyngid
"""

import platform
import sys

from .exceptions import *

if platform.system() != 'Windows':
  raise Exception('This module is only for Windows')
del platform

if sys.version_info < (3, 5):
  raise PyngidUnsupportedError('This module requires Python 3.5 or higher')
del sys
