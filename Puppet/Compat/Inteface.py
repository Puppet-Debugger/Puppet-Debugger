from .CompatExecution import QilingRun
from .CompatOS import QilingIO, QilingFs, QilingMem
from .CompatDebug import QilingHook
from .CompatHardware import QilingReg


class Compat(QilingRun,  # Execution
             QilingIO, QilingFs, QilingMem,  # OS
             QilingHook,  # Debug
             QilingReg  # Hardware
             ):
    pass
