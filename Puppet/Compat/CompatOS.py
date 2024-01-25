from os import PathLike
from typing import Union, Any, AnyStr

from qiling import Qiling
from qiling.extensions import pipe

from Puppet.Auxiliary.Data import SegmentType, PermissionType


class QilingMem:
    ql: Qiling

    def mem_read(self, address: int, size: int):
        return self.ql.mem.read(address, size)

    def mem_write(self, address: int, data: bytes):
        self.ql.mem.write(address, data)

    def mmap_read(self):
        return self.ql.mem.get_mapinfo()

    def mmap_filter(self, segment_type: SegmentType = None, permission_type: PermissionType = None):
        mmap_output = self.ql.mem.get_mapinfo()

        def segment_length(mem_seg_start, mem_seg_end):
            return mem_seg_end - mem_seg_start

        def is_executable(mem_seg_start, mem_seg_end):
            # 示例条件，实际条件根据需要调整
            # 和文件类型强相关，后期需要进行多态调整
            return mem_seg_start < 0x555555566000

        filtered_segments = []
        for segment in mmap_output:
            start, end, perms, name, _ = segment
            if permission_type.value and permission_type.value not in perms:
                continue

            if segment_type.value:
                if segment_type.value == 'executable' and not is_executable(start, end):
                    continue
                if segment_type.value == 'heap' and 'heap' not in name:
                    continue
                if segment_type.value == 'libc' and 'libc' not in name:
                    continue
                if segment_type.value == 'ld' and 'ld' not in name:
                    continue
                if segment_type.value == 'stack' and 'stack' not in name:
                    continue
                if segment_type.value == 'other' and any(
                        keyword in name for keyword in ['heap', 'libc', 'ld', 'stack']):
                    continue

            filtered_segments.append((start, end, segment_length(start, end), name))

        return filtered_segments


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
