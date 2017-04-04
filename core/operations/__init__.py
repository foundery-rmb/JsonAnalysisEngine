from JsonAnalysisEngine.utils import JsonObject
from JsonAnalysisEngine.internal.factory import Factory
from JsonAnalysisEngine.core.exceptions import BindError, ElementBuildError

from JsonAnalysisEngine.core.domain import json_domain as domain
import weakref


class NodeExplorer(object):
    
    def __init__(self):
        self.json_data = None

    def set_data(self, data):
        self.json_data = data

    def on_traversal(self, node_info):
        """
        this method is hooked on the `json_traversal` recursion loop
        """
        node_class = domain.get_node_type(node_info)  # returns ValueNode, ListNode or TreeNode class
        node = Factory.create_object(node_class, node_info)  # instantiate the class
        print node

    def attach_action(self, action):
        """
        this method is used to attach an action to be performed on the node
        """
        pass

    def on_done(self, status):
        """
        this method is called when the traversal process is done
        """
        pass

    def start_session(self, **kwargs):
        """
        This is used to start the traversal process and build a dataset
        """
        coreop = Factory.CoreOperations
        coreop.bind(on_traversal=self.on_traversal)
        coreop.bind(on_traversal_done=self.on_done)
        if not self.json_data:
            raise ElementBuildError("No json data set to ElementBuilder")
        Factory.CoreOperations.start_traversing(self.json_data)
    

class CoreOperations(object):
    """
    This class is the heart of the jae (json analysis engine), this class is responsible for providing
    capabilities to build node datasets which are essential in running the analysis component
    """

    binds = {'on_traversal': [], 'on_traversal_done': []}
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
        bind_list.append(function)
        return True

    def _on_traversal(self, info):
        """
        This is dispatched when the traversal algorithm is active.
        """

        map(lambda func: func(info), self.binds['on_traversal'])


    def _on_traversal_done(self, info):
        """
        this acts as a dispatcher to all functions hooked to the on_done
        event
        """
        map(lambda func: func(info), self.binds['on_traversal_done'])

    def start_traversing(self, json_data):
        """
        this method starts the traversal algorithm
        """

        def _callback(info, event='on_traversal'):
            """
            This callback function will process info and call bound methods
            """
            if info is None:
                return self._on_traversal_done(info)
            if isinstance(info.value, dict):
                info['value'] = JsonObject(info.value)
            if isinstance(info.key, dict):
                info['key'] = JsonObject(info.key)
            if event == 'on_traversal':
                self._on_traversal(info)
            elif event == 'on_traversal_done':
                self._on_traversal_done(info)
            else:
                raise ValueError('No callback event named %s' % event)
        self.json_traversal(json_data, _callback)

    def json_traversal(self, json_dict, func, depth=0):
        """
        This is the main traversal algorithm of the JAEngine. While traversing through the
        tree the algorithm calls `func`.
        """

        info = JsonObject({'depth': depth})
        parent = json_dict
        for key in json_dict.keys():
            info['key'] = key
            info['value'] = json_dict[key]
            info['parent'] = parent
            func(info, event='on_traversal')
            if isinstance(json_dict[key], dict):
                self.json_traversal(json_dict[key], func, depth + 1)
            if isinstance(json_dict[key], list):
                for val in json_dict[key]:
                    if isinstance(val, dict):
                        self.json_traversal(val, func, depth)
        func(None, event='on_done')

Factory.register('CoreOperations', cls=CoreOperations())
Factory.register('ElementBuilder', cls=NodeExplorer())
