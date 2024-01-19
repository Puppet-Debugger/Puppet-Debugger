from typing import Optional

from qiling import Qiling


class QilingRun:
    ql: Qiling
    begin: Optional[int] = None
    end: Optional[int] = None
    timeout: int = 0
    count: int = 0

    def exec_run(self):
        self.ql.run(begin=self.begin, end=self.end, timeout=self.timeout, count=self.count)

    def exec_set_begin_end(self, begin, end):
        self.begin = begin
        self.end = end

    def exec_set_timeout(self, timeout):
        self.timeout = timeout

    def exec_set_count(self, count):
        self.count = count
