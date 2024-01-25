from typing import Optional

from qiling import Qiling


class QilingRun:
    ql: Qiling
    __begin: Optional[int] = None
    __end: Optional[int] = None
    __timeout: int = 0
    __count: int = 0

    def exec_run(self):
        self.ql.run(begin=self.__begin, end=self.__end, timeout=self.__timeout, count=self.__count)
        self.__begin = None
        self.__end = None
        self.__timeout = 0
        self.__count = 0

    def exec_set_begin_end(self, begin, end):
        self.__begin = begin
        self.__end = end

    def exec_set_timeout(self, timeout):
        self.__timeout = timeout

    def exec_set_count(self, count):
        self.__count = count
