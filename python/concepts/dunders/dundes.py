"""
Dunders are special methods in Python that have double underscores at the beginning and end of their names.
"""

class Human:
    """Human class"""
    name: str = None
    def __init__(self, name):
        self.name = name
print(Human.__dict__) # {'__module__': '__main__', '__doc__': 'Human class', 'name': None, '__init__': <function Human.__init__ at 0x7f8b1c1b7d30>}