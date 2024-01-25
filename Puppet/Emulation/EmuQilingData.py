from typing import Sequence, MutableMapping, AnyStr, Optional
from enum import Enum
from dataclasses import dataclass

from qiling import Qiling
from qiling.const import QL_OS, QL_ARCH, QL_ENDIAN, QL_VERBOSE


# 对 verbose, endian 标志词的封装
class VerboseLevel(Enum):
    DEBUG: QL_VERBOSE = QL_VERBOSE.DEBUG
    OFF: QL_VERBOSE = QL_VERBOSE.OFF
    DISABLED: QL_VERBOSE = QL_VERBOSE.DISABLED
    DISASM: QL_VERBOSE = QL_VERBOSE.DISASM


class EndianType(Enum):
    EB = QL_ENDIAN.EB
    EL = QL_ENDIAN.EL


@dataclass
class BinaryArgs:
    argv: Sequence[str]
    rootfs: str
    env: Optional[MutableMapping[AnyStr, AnyStr]]
    verbose: str
    profile: Optional[str]
    multithread: bool
    libcache: bool
    ql: Qiling = None


@dataclass
class ShellcodeArgs:
    code: bytes
    ostype: QL_OS
    archtype: QL_ARCH
    rootfs: Optional[str]
    endian: Optional[QL_ENDIAN]
    thumb: bool
    verbose: str
    profile: Optional[str]
    multithread: bool
    libcache: bool
    ql: Qiling = None
