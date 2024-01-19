from os import PathLike
from typing import Union, Any, AnyStr

from qiling import Qiling
from qiling.extensions import pipe


class QilingMem:
    ql: Qiling

    def mem_read(self, address: int, size: int):
        return self.ql.mem.read(address, size)

    def mem_write(self, address: int, data: bytes):
        self.ql.mem.write(address, data)


class QilingFs:
    ql: Qiling

    def fs_add(self, vfs_path: Union[PathLike, str], real_dest: Any):
        # 检查映射是否已经存在
        if self.ql.os.fs_mapper.has_mapping(vfs_path):
            raise ValueError(f"Mapping '{vfs_path}' already exists.")
        self.ql.os.fs_mapper.add_mapping(vfs_path, real_dest)

    def fs_del(self, vfs_path: Union[PathLike, str]):
        # 检查映射是否存在
        if not self.ql.os.fs_mapper.has_mapping(vfs_path):
            raise KeyError(f"Mapping '{vfs_path}' does not exist.")
        self.ql.os.fs_mapper.remove_mapping(vfs_path)

    def fs_num(self) -> int:
        # 返回建立的映射数，用于上层检查合法性
        return self.ql.os.fs_mapper.mapping_count()


class QilingIO:
    ql: Qiling

    def io_set_in(self, fd: int):
        self.ql.os.stdin = pipe.SimpleInStream(fd)

    def io_set_out(self, fd: int):
        self.ql.os.stdout = pipe.SimpleOutStream(fd)

    def io_set_err(self, fd: int):
        self.ql.os.stderr = pipe.SimpleOutStream(fd)

    def io_write_in(self, data: AnyStr):
        self.ql.os.stdin.write(data)

    def io_read_out(self, length: int):
        return self.ql.os.stdout.read(length)

    def io_read_err(self, length: int):
        return self.ql.os.stderr.read(length)