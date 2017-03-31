import abc

# A list of classes to categorize nodes

class BaseNode:
    __metaclass__ = abc.ABCMeta


class IValueNode(BaseNode):
    pass

class ITreeNode(BaseNode):
    pass


class IListNode(BaseNode):
    pass


class IValueListNode(BaseNode):
    pass


class IValue(BaseNode):
    pass