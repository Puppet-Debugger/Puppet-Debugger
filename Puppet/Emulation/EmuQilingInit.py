"""
此文件包含了对Qiling的封装与Hook扩展层相关实现
Qiling封装的相关函数与类:
    QilingEmulatorBase类:Qiling的通用操作
    Binary类:对Qiling的二进制仿真模式的封装
    Shellcode类:对Qiling的Shellcode仿真模式的封装
"""

from logging import FileHandler
from typing import Sequence, MutableMapping, AnyStr

from qiling import Qiling
from qiling.const import QL_OS, QL_ARCH

from Puppet.Auxiliary.Data import Main_Data
from Puppet.Auxiliary.Extension import Binary_Before_Extension_Manager, Binary_After_Extension_Manager, \
    Shellcode_Before_Extension_Manager, Shellcode_After_Extension_Manager

from Puppet.Emulation.EmuQilingData import BinaryArgs, ShellcodeArgs, VerboseLevel, EndianType

from Puppet.Compat.Inteface import Compat


# 二进制仿真类，封装了 Qiling 的二进制仿真模式
class Binary(Compat):
    def __init__(self, argv: Sequence[str], rootfs: str, env: MutableMapping[AnyStr, AnyStr] = None,
                 verbose: VerboseLevel = VerboseLevel.OFF, profile: str = None,
                 multithread: bool = False, libcache: bool = False
                 ):

        # 参数验证
        if not isinstance(argv, Sequence) or not all(isinstance(arg, str) for arg in argv):
            raise ValueError("argv must be a sequence of strings.")
        if not isinstance(rootfs, str):
            raise ValueError("rootfs must be a string.")
        if env is not None and not isinstance(env, MutableMapping):
            raise ValueError("env must be a mutable mapping or [].")
        if profile is not None and not isinstance(profile, str):
            raise ValueError("profile must be a string.")

        # Hook扩展
        extension_args = BinaryArgs(argv=argv, rootfs=rootfs, env=env or {},
                                    verbose=verbose.value, profile=profile,
                                    multithread=multithread, libcache=libcache
                                    )
        Binary_Before_Extension_Manager.execute_functions(extension_args)

        # 创建 Qiling 对象
        self.ql = Qiling(argv, rootfs, env=env or {},
                         verbose=verbose.value, profile=profile,
                         multithread=multithread, libcache=libcache
                         )

        extension_args.ql = self.ql
        Binary_After_Extension_Manager.execute_functions(extension_args)

        # 分离仿真程序输出与日志输出
        file_handler = FileHandler(Main_Data.get_log_file_path("tmp/Binary.log"))
        self.ql.log.handlers = []
        self.ql.log.addHandler(file_handler)


# Shellcode 仿真类，封装了 Qiling 的 Shellcode 仿真模式
class Shellcode(Compat):
    def __init__(self, code: bytes, ostype: QL_OS, archtype: QL_ARCH,
                 rootfs: str = None, endian: EndianType = EndianType.EL, thumb: bool = False,
                 verbose: VerboseLevel = VerboseLevel.OFF, profile: str = None,
                 multithread: bool = False, libcache: bool = False
                 ):

        # 参数验证
        if not isinstance(code, bytes):
            raise ValueError("code must be bytes.")
        if not isinstance(ostype, QL_OS):
            raise ValueError("ostype must be a QL_OS instance or None.")
        if not isinstance(archtype, QL_ARCH):
            raise ValueError("archtype must be a QL_ARCH instance or None.")
        if rootfs is not None and not isinstance(rootfs, str):
            raise ValueError("rootfs must be a string or None.")
        if not isinstance(thumb, bool):
            raise ValueError("thumb must be a boolean.")

        # Hook扩展
        extension_args = ShellcodeArgs(code=code, ostype=ostype, archtype=archtype,
                                       rootfs=rootfs, endian=endian.value, thumb=thumb,
                                       verbose=verbose.value, profile=profile,
                                       multithread=multithread, libcache=libcache
                                       )
        Shellcode_Before_Extension_Manager.execute_functions(extension_args)

        # 创建 Qiling 对象
        self.ql = Qiling(code=code, ostype=ostype, archtype=archtype,
                         rootfs=rootfs, endian=endian.value, thumb=thumb,
                         verbose=verbose.value, profile=profile,
                         multithread=multithread, libcache=libcache
                         )
        extension_args.ql = self.ql
        Shellcode_After_Extension_Manager.execute_functions(extension_args)

        # 分离仿真程序输出与日志输出
        file_handler = FileHandler(Main_Data.get_log_file_path("tmp/Shellcode.log"))
        self.ql.log.handlers = []
        self.ql.log.addHandler(file_handler)