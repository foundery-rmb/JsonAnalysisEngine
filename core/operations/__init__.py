from JsonAnalysisEngine.utils import JsonObject
from JsonAnalysisEngine.core.exceptions import BindError
from JsonAnalysisEngine.core.domain.json_domain import BaseNode
from JsonAnalysisEngine.core.domain.json_domain import ListNode
from JsonAnalysisEngine.core.domain.json_domain import TreeNode
from JsonAnalysisEngine.core.domain.json_domain import TreeNode
from JsonAnalysisEngine.core.domain.json_domain import ValueNode
from JsonAnalysisEngine.core.domain.json_domain import ValueListNode

import weakref


class NodeExplorer(object):
    
    def on_traversal(self, node_info):
        """
        this method is hooked on the `json_traversal` recursion loop
        """
        pass

    def attach_action(self, action):
        """
        this methof is used to attach an action to be performed on the node
        """
        pass
    

class CoreOperations(object):
    """
    This class is the heart of the jae (json analysis engine), this class is responsible for providing
    capabilities to build node datasets which are essential in running the analysis component
    """

    binds = {'on_traversal': []}
    on_traversal_binds = {}

    def bind(self, **kwargs):
        """
        This method is used to bind functions to events of the core operations
        """
        
        if not kwargs:
            raise ValueError("no key word argument provided")
        key = kwargs.keys()[0]
        function = kwargs[key]
        bind_list = self.binds.get(key, None)
        if bind_list is None:
            raise BindError('could not bind to event %s' % key)
        bind_list.append(weakref.proxy(function))
        return True

    @staticmethod
    def _on_traversal(info):
        """
        This is dispatched when the traversal algorithm is active.
        """

        for func in self.binds['on_traversal']:
            func(info)

    @staticmethod
    def json_traversal(json_dict, func, depth=0):
        """
        This is the main traversal algorithm of the JAEngine. While traversing through the
        tree the algorithm calls `func`.
        """

        info = JsonObject({'depth': depth})
        parent = json_dict
        for key in json_dict.keys():
            info['key'] = key
            info['value'] = json_dict[key]
            info['parent'] = json_dict
            func(info)
            if isinstance(json_dict[key], dict):
                json_traversal(json_dict[key], func, depth + 1)
            if isinstance(json_dict[key], list):
                for val in json_dict[key]:
                    if isinstance(val, dict):
                        json_traversal(val, func, depth)