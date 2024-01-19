from typing import Sequence, MutableMapping, AnyStr, Optional
from dataclasses import dataclass

from qiling import Qiling
from qiling.const import QL_OS, QL_ARCH, QL_ENDIAN


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
