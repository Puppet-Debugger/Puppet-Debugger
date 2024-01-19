from Puppet import Puppet
from Puppet import Main_Data

from qiling import Qiling
from qiling.extensions import pipe
import os
import time

pu = Puppet(["../Config/rootfs/x8664_linux_u20/bin/sh"],
            "../Config/rootfs/x8664_linux_u20",
            multithread=True,
            verbose="d"
            )


# def qiling_io_test(_pu: Puppet):
#     _pu.io_set_in(0)
#     _pu.io_set_out(1)
#     _pu.io_set_out
#     _pu.exec_run()
#     print(_pu.io_read_out(100))


# Main_Data.del_log_file()
# qiling_io_test(pu)

pu.exec_run()