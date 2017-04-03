from JsonAnalysisEngine.interfaces.domain.json_domain import BaseNode
from JsonAnalysisEngine.interfaces.domain.json_domain import IListNode
from JsonAnalysisEngine.interfaces.domain.json_domain import ITreeNode
from JsonAnalysisEngine.interfaces.domain.json_domain import IValueNode
from JsonAnalysisEngine.interfaces.domain.json_domain import IValueListNode



class BaseNode(BaseNode):
    
    def __init__(self): pass

    def get_parent(self): pass

    def get_all_nodes_with_same_value(self): pass

    def get_number_of_occurances(self): pass


class ListNode(BaseNode, IListNode):
    pass


class TreeNode(BaseNode, ITreeNode):
    pass


class ValueListNode(BaseNode, IValueListNode):
    pass


class ValueNode(BaseNode, IValueNode):
    pass
