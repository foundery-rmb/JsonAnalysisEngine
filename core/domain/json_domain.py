
class BaseNode(object):
    
    def __init__(self, value):
        if isinstance(value, dict):
            self.raw_json = value

    def get_parent(self):
        return self.raw_json.parent

    def get_all_nodes_with_same_value(self): pass

    def get_number_of_occurances(self): pass


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