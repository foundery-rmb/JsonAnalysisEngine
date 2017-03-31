import abc

# A list of classes to categorize nodes

class BaseNode:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_parent(): pass

    @abc.abstractmethod
    def get_all_nodes_with_same_value(): pass

    @abc.abstractmethod
    def get_number_of_occurances(): pass


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

