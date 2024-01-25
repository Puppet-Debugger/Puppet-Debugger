from qiling import Qiling
from qiling.extensions import pipe
from qiling.const import QL_VERBOSE
import os
import time

from Auxiliary.Data import RegArmType
from Puppet.Emulation.EmuQilingInit import Binary
from Puppet.Emulation.EmuQilingData import VerboseLevel
from Puppet import HookType


pu = Binary(["../Config/rootfs/arm64_linux/bin/arm64_hello"],
            "../Config/rootfs/arm64_linux",
            multithread=False,
            verbose=VerboseLevel.OFF
            )

# def qiling_io_test(_pu: Puppet):
#     _pu.io_set_in(0)
#     _pu.io_set_out(1)
#     _pu.io_set_out
#     _pu.exec_run()
#     print(_pu.io_read_out(100))


# Main_Data.del_log_file()
# qiling_io_test(pu)

pu.ql.verbose = QL_VERBOSE.DISASM
iz = 0
iu = 0

begin_time = time.time()


def dbg_hook(ql: Qiling, address, size):
    global iz
    iz += 1
    print(iz, hex(pu.ql.arch.regs.arch_pc))


def dbg_hook2(ql: Qiling, address, size, _f1):
    global iz, iu
    iz += 1
    print(iz, hex(pu.ql.arch.regs.arch_pc), "#")
    if iz >= 0x500 and iu == 0:
        iu = 1
        pu.hook_del(_f1)
    if iz >= 0x1000:
        pu.ql.stop()

# def dbg_hook3(ql: Qiling, address, size):
#     pc = pu.ql.arch.regs.arch_pc


pu.hook_add(HookType.CODE, dbg_hook)
pu.hook_add(HookType.CODE, dbg_hook2, dbg_hook)
pu.exec_run()

print(pu.reg_read_args())

end_time = time.time()
print(end_time - begin_time)
