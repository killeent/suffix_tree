"""
Implementation of a naive suffix trie. 
"""


class SuffixTrieNode(object):
    """
    A suffix trie node is composed of two things:

    1. A suffix link. Suppose the node n represents some suffix "xb", where
    x is a single character and b is a sequence of characters. A suffix link
    will link to a SuffixTrieNode p representing the suffix b. So if n is
    the string"abbaa", then it will point to a node representing the string
    "bbaa".

    Because every node in the graph represents the prefix to some suffix in
    the input string, we are guaranteed to have a valid suffix link for every
    node in the trie, except for the root.

    2. A set of edges to children SuffixTrieNode. Edges are mappings from
    character labels of the edge to SuffixTrieNode children. For example, if
    some SuffixTrieNode n represents the suffix "abcd" and has an edge
    mapping of 'e' => SuffixTrieNode p, then p represents the suffix
    "abcde".
    """

    def __init__(self, suffix_link=None):
        """
        Constructs a new SuffixTrieNode.

        Args:
            suffix_link a suffix_link for this node as described above.
        """
        self.suffix_link = suffix_link
        self.edges = {}

    def add_edge(self, label, child):
        """
        Adds an an edge to this SuffixTrieNode with the specified label.

        Args:
            label the label for the edge
            child a SuffixTrieNode as described above
        """
        self.edges[label] = child

    def contains_edge(self, label):
        """
        Checks and see if this SuffixTrieNode has the specified edge.

        Returns:
            True if we have the edge, otherwise false
        """
        return label in self.edges

    def get_edge(self, label):
        """
        Get the SuffixTrieNode associated with the label if it exists.

        Args:
            label identifies the edge

        Returns:
            the SuffixTrieNode add the end of the edge if it exists.
        """
        return self.edges[label]

    def edge_list(self):
        """
        Return the list of edges originating in this SuffixTrieNode.

        Returns:
            the list of edges originating in this SuffixTrieNode.
        """
        return self.edges.values()

    def add_link(self, suffix_link):
        """
        Adds an an suffix_link to this SuffixTrieNode.

        Args:
            suffix_link the SuffixTrieNode to link to.
        """
        self.suffix_link = suffix_link

    def get_link(self):
        """
        Get the SuffixTrieNode linked to by this node.

        Returns:
            the SuffixTrieNode linked to edge if it exists.
        """
        return self.suffix_link


def _build_suffix_trie(string):
    """
    Constructs a suffix trie from the specified string.

    Args:
        string the string to construct a suffix trie from

    Returns:
        a SuffixTrieNode that is the root of the constructed suffix_trie
    """

    # explicitly construct root and first child
    root = SuffixTrieNode()

    if len(string) == 0:
        return root

    deepest = SuffixTrieNode(root)
    root.add_edge(string[0], deepest)

    # while there are elements remaining in the string, add
    # them as children to every leaf in the suffix trie, and
    # the root

    for character in string[1:]:
        curr = deepest
        prev = None

        # iterate until we run out of nodes to add the label
        # to (i.e. we have added it to root) or the current node already
        # has the specified label as a child
        while curr is not None and not curr.contains_edge(character):
            child = SuffixTrieNode()
            curr.add_edge(character, child)

            # add a suffix link to this new node if necessary
            if prev is not None:
                prev.add_link(child)

            # iterate
            prev = child
            curr = curr.get_link()

        # if curr is not None, then the current node already contains the
        # specified character as an edge, so we must update the
        # suffix_link of prev to point to that edge
        if curr is not None:
            prev.suffix_link = curr.get_edge(character)

        # update the deepest node in the trie to be the child of
        # the previous deepest node
        deepest = deepest.get_edge(character)

    return root


def substring(suffix_trie, search_str):
    """
    Given a suffix_trie representation of a string, determines if search_str
    is a substring of that suffix tree'd string.

    Args:
        suffix_trie a suffix_trie representation of a tree
        search_str the substring to search for

    Returns:
        True if search_str is a substring of suffix_trie, otherwise False.
    """

    curr = suffix_trie
    for c in search_str:
        curr = curr.get_edge(c)
        if curr is None:
            return False

    return True


def suffix(suffix_trie, suffix_str):
    """
    Given a suffix_trie representation of a string, determines if suffix_str
    is a suffix of that suffix tree'd string.

    Args:
        suffix_trie a suffix_trie representation of a tree
        suffix_str the substring to search for

    Returns:
        True if suffix_str is a suffix of suffix_trie, otherwise False.
    """

    curr = suffix_trie
    for c in suffix_str:
        curr = suffix_trie.get_edge(c)
        if curr is None:
            return False

    # check and see if we are leaf
    return len(curr.edge_list()) == 0


def occurrences(suffix_trie, search_str):
    """
    Given a suffix_trie representation of a string, returns the number of
    occurrences of search_str in the suffix_trie.

    Args:
        suffix_trie a suffix_trie representation of a tree
        search_str the substring to search for

    Returns:
        The number of occurrences of search_str in suffix_trie.
    """

    curr = suffix_trie
    for c in search_str:
        curr = curr.get_edge(c)
        if curr is None:
            return 0

    # count the number of leaves below this
    return _get_leaves(suffix_trie)


def _get_leaves(suffix_trie):
    """
    Counts the number of leaves in the suffix_trie.

    Args:
        suffix_trie the root SuffixTrieNode of the suffix_trie.

    Returns:
        The number of leaves in the suffix_trie.
    """
    if len(suffix_trie.edge_list()) == 0:
        return 1
    else:
        return sum([_get_leaves(x) for x in suffix_trie.edge_list()])


def main():
    """
    Constructs a trie, and runs some queries on it.
    """
    trie = _build_suffix_trie("abaaba")

if __name__ == '__main__':
    main()