"""
Tests for the naive suffix trie.
"""

import pytest
from suffixtree import naive_suffix_trie


class TestBuildSuffixTrie:

    def test_build_empty_suffix_trie(self):
        trie = naive_suffix_trie.build_suffix_trie("")

