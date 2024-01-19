class ExtensionManager:
    def __init__(self):
        self.functions = []

    def add_function(self, func):
        """添加函数到列表中"""
        if callable(func):
            self.functions.append(func)
        else:
            raise ValueError("Provided object is not callable")

    def remove_function(self, func):
        """从列表中移除函数"""
        self.functions.remove(func)

    def execute_functions(self, data):
        """按顺序执行所有函数"""
        for func in self.functions:
            func(data)


Binary_Before_Extension_Manager: ExtensionManager = ExtensionManager()
Binary_After_Extension_Manager: ExtensionManager = ExtensionManager()
Shellcode_Before_Extension_Manager: ExtensionManager = ExtensionManager()
Shellcode_After_Extension_Manager: ExtensionManager = ExtensionManager()
