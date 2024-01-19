"""Puppet - Cross-Platform Timeless Compat and Static Analysis Component Library Built on Qiling"""
__version__ = '0.1.0'
__author__ = 'Alsoprach <Alsoprach@gmail.com>'

from .core import Puppet
from .Utility.DataManager import Main_Data

__all__ = [Puppet, Main_Data]

# Puppet Extension Initialization
from .Extension.EmuQilingPatch import patch_ld_cpu_isa_check_x8664
from .Utility.ExtensionManager import Binary_After_Extension_Manager

Binary_After_Extension_Manager.add_function(patch_ld_cpu_isa_check_x8664)
