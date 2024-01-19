from typing import Union

import qiling
import os
from qiling.const import QL_INTERCEPT

from Puppet.Emulation.EmuQilingData import ShellcodeArgs, BinaryArgs


def null_rseq_impl(__ql: qiling.Qiling, abi: int, length: int, flags: int, sig: int):
    return 0


def get_ld_base(ql: qiling.Qiling):
    mmap_info = ql.mem.get_mapinfo()
    base: int = 0
    end: int = 0
    first_flag: bool = True
    for element in mmap_info:
        filename = os.path.basename(element[-1])
        if filename.startswith("ld-"):
            if first_flag:
                base = element[0]
                first_flag = False
            end = element[1]
    return base, end


def address_cpu_isa_check_jz(ql: qiling.Qiling, __ld_base: int, __ld_end: int):
    code = (b"\x74\x19" +          # jz      short loc_23894
            b"\x48\x39\x7a\x28" +  # cmp     [rdx+28h], rdi
            b"\x74\x13")           # jz      short loc_23894
    return ql.mem.search(code, __ld_base, __ld_end)


def patch_ld_cpu_isa_check_x8664(data: Union[BinaryArgs, ShellcodeArgs]):
    data.ql.os.set_syscall('rseq', null_rseq_impl, qiling.const.QL_INTERCEPT.CALL)
    ld_base, ld_end = get_ld_base(data.ql)

    if data.ql.mem.search("GLIBC 2.35".encode(), ld_base, ld_end):
        if ld_base:
            data.ql.mem.write(address_cpu_isa_check_jz(data.ql, ld_base, ld_end)[0] + 0x6, b"\xeb")
        else:
            print("Don't Find [ld-linux-x86-64.so.2]")

