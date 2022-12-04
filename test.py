
dt = 0.20000
discount = 0.99005

u = 1.17468
d = 0.85129

class Node:
    def __init__(self, price) -> None:
        self.price = price
        self.up = None
        self.down = None
        self.hori = None
        self.level = 0

def build(node: Node):
    
    if node.level < 5:
        if node.up is None:
            node.up = Node(node.price * u)
            node.up.level += 1
            build(node.up)
        if node.hori is None:
            node.hori = Node(node.price)
            node.hori.level += 1
            build(node.hori)
        if node.down is None:
            node.down = Node(node.price * d)
            node.down.level += 1
            build(node.down)
    return None

root = Node(100)
n_step = 5
build(root)
