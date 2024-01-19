import os


class DataManager:
    LogFile_Path: str

    def __init__(self) -> None:
        self.root = os.path.join(*[os.path.dirname(os.path.abspath(__file__))] + [".."] * 1)

    # 日志管理函数
    def get_log_file_path(self, relative_path) -> str:
        self.LogFile_Path = os.path.join(self.root, relative_path)
        return self.LogFile_Path

    def del_log_file(self):
        os.remove(self.LogFile_Path)

    def data_del(self):
        """
        数据终末化函数
        """
        self.del_log_file()


Main_Data: DataManager = DataManager()