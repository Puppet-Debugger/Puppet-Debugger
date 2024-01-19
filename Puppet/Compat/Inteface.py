from .CompatExecution import QilingRun
from .CompatOS import QilingIO, QilingFs, QilingMem


class Compat(QilingRun,
             QilingIO, QilingFs, QilingMem
             ):
    pass
