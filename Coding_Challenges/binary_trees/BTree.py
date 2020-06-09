class Tree():
    """
    Class Tree needs to be inherited with each challenge's solution.
    Each challenge needs to implement run_it() where its requested features are ran.
    """
    def __init__(self, root):
        self.root = root
    
    def run_it(self):
        """
        This method needs to be implemented by Tree's children.
        """
        raise NotImplemented()
    
    @classmethod
    def total(cls, tree):
        raise NotImplemented()
    
    def total_me(self):
        return self.total(self)


class Node():
    
    def __init__(self, val, left=None, right=None):
        self.__val = val
        self.__left = left
        self.__right = right
    
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_left(self, node):
        self.__left = node
    
    def set_right(self, node):
        self.__right = node