"""Puppet - Cross-Platform Timeless Compat and Static Analysis Component Library Built on Qiling"""
__version__ = '0.1.0'
__author__ = 'Alsoprach <Alsoprach@gmail.com>'

from Puppet.Auxiliary.Data import HookType, SegmentType, PermissionType, RegArmType

__all__ = [HookType, SegmentType, PermissionType, RegArmType]

# Puppet Extension Initialization
from .Extension.EmuQilingPatch import patch_ld_cpu_isa_check_x8664
from .Auxiliary.Extension import Binary_After_Extension_Manager

Binary_After_Extension_Manager.add_function(patch_ld_cpu_isa_check_x8664)
