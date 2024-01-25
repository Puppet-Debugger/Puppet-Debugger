from qiling import Qiling
from qiling.const import QL_ARCH
from Puppet.Auxiliary.Data import RegArmType, ArchType


class QilingReg:
    ql: Qiling

    def reg_read(self, reg: RegArmType) -> int:
        """读取寄存器的值"""
        return self.ql.arch.regs.read(reg.value)

    def reg_write(self, reg: RegArmType, value: int) -> None:
        """写入值到寄存器"""
        self.ql.arch.regs.write(reg.value, value)

    def reg_read_pc(self):
        return self.ql.arch.regs.arch_pc

    def reg_write_pc(self,value: int):
        self.ql.arch.regs.arch_pc = value

    def reg_read_sp(self):
        return self.ql.arch.regs.arch_sp

    def reg_write_sp(self, value: int):
        self.ql.arch.regs.arch_sp = value

    def reg_read_args(self):
        # 定义不同架构下的函数传参寄存器
        registers = {
            "x86": [],  # 在x86架构中，参数通常通过栈传递
            "x86_64": ["rdi", "rsi", "rdx", "rcx", "r8", "r9"],
            "arm": ["r0", "r1", "r2", "r3"],
            "arm64": ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
        }
        arch = ArchType[self.ql.arch.type.name].value
        # 返回对应架构的传参寄存器列表
        reg_value = []
        for reg in registers.get(arch.lower(), []):
            reg_value.append(self.ql.arch.regs.read(reg))
        return reg_value
