from qiling import Qiling

from Puppet.Auxiliary.Data import HookType


class QilingHook:
    ql: Qiling
    hook_dict = {}

    def hook_add(self, hook_type: HookType, callback, user_data=None, begin=1, end=0):
        hook_function = getattr(self.ql, hook_type.value)
        hook_id = hook_function(callback, user_data, begin, end)
        self.hook_dict[callback] = hook_id

    def hook_del(self, callback):
        if callback in self.hook_dict:
            hook_id = self.hook_dict.pop(callback)
            self.ql.hook_del(hook_id)
        else:
            raise ValueError("Hook not found")
