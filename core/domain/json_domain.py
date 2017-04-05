
from jae.internal.factory import Factory


class BaseNode(object):
    value = None
    key = None
    parent = None

    def __init__(self, value):
        if isinstance(value, dict):
            self.raw_json = value

    def get_parent(self):
        node_table = Factory.NodeTable
        self.parent = node_table.get_node(hash(self.raw_json.parent))
        return self.parent
        

    def get_value(self):
        return self.raw_json.value

    def get_all_nodes_with_same_value(self): pass

    def get_number_of_occurances(self): pass

    def hash(self):
        return hash(self.raw_json)

class NullNode(object):
    pass


class ListNode(BaseNode):
    pass


class TreeNode(BaseNode):
    pass


class ValueNode(BaseNode):
    pass


def get_node_type(json_data):
    """
    returns the node type of `json_data` can either `ValueNode`, `ValueListNode`, etc
    """

    if isinstance(json_data.value, dict):
        return TreeNode
    elif isinstance(json_data.value, list):
        return ListNode
    else:
        return ValueNode