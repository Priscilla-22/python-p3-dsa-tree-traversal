from collections import deque


class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):

        # depth-first traversal
        def depthFirst(node):
            if node is None:
                return None
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = depthFirst(child)
                if result:
                    return result
            return None

        return depthFirst(self.root)

    # breadth first search
    def get_element_by_id2(self, id):
        if self.root is None:
            return None

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.get('id') == id:
                return node
            queue.extend(node.get('children', []))

        return None
