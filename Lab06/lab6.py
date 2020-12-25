
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.
    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    if label(t) == 'acorn':
        return True
    for b in branches(t):
        if acorn_finder(b):
            return True
    return False

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears
    in vals removed. Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
        2
        3
            4
            5
        6
            7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
        2
        3
            5
        6
    """
    if is_leaf(t) and (label(t) in vals):
        return None
    new_branches = []
    for b in branches(t):
        new_branch = prune_leaves(b, vals)
        if new_branch:
            new_branches += [new_branch]
    return tree(label(t), new_branches)


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
        2
        3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
        2
            4
            5
        3
            4
            5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
        2
            3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
        2
            3
                6
                1
                2
    """
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in vals])
    return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max(height(b) for b in branches(t))


def double_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
                        [tree(2,
                                [tree(3),
                                tree(4)]),
                        tree(5,
                                [tree(6,
                                        [tree(7)]),
                                tree(8)])])
    >>> print_tree(double_tree(numbers))
    2
        4
            6
            8
        10
            12
                14
            16
    """
    double_branches = [double_tree(brance) for brance in branches(t)]
    return tree(label(t) * 2, double_branches)

def add_trees(t1, t2):
    """
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]),tree(5, [tree(6, [tree(7)]),tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
        4
            6
            8
        10
            12
                14
            16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
        4
        5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
        6
        4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
        6
            8
            5
        5
    """
    if not t1:
        return t2
    if not t2:
        return t1
    new_label = label(t1) + label(t2)
    t1_children, t2_children = branches(t1), branches(t2)
    length_t1, length_t2 = len(t1_children), len(t2_children)
    if length_t1 < length_t2:
        t1_children += [None for i in range(length_t1, length_t2)]
    elif length_t1 > length_t2:
        t2_children += [None for i in range(length_t2, length_t1)]
    return tree(new_label, [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)])





