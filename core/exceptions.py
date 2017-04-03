

class Error(Exception):
    """
    Standard base error
    """


class BindError(Error):
    """
    This is raised when someone tries to bind an action to the action/event/time dispatcher
    that doesn't have exist
    """


class EngineCrash(Error):
    """
    This is raised during a catastrophic crash or error
    """

class ElementBuildError(Error):
    pass