"""
Tests for the naive suffix trie.
"""

import pytest
from suffixtree import naive_suffix_trie


class TestBuildSuffixTrie:

    def test_build_empty_suffix_trie(self):
        """
        Tests building an empty suffix trie.
        """
        naive_suffix_trie.build_suffix_trie('')

    def test_build_single_element_suffix_trie(self):
        """
        Tests building a single-element suffix trie.
        """
        naive_suffix_trie.build_suffix_trie('a')

    def test_build_multi_element_suffix_trie(self):
        """
        Tests building a multi-element suffix trie.
        """
        naive_suffix_trie.build_suffix_trie('abc')


class TestSubstring:

    def test_substring_empty_trie(self):
        """
        Tests substring operations on an empty trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('')
        assert naive_suffix_trie.substring(trie, '')
        assert not naive_suffix_trie.substring(trie, 'a')

    def test_substring_single_element_trie(self):
        """
        Tests substring operations on a single element trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('a')
        assert naive_suffix_trie.substring(trie, '')
        assert naive_suffix_trie.substring(trie, 'a')
        assert not naive_suffix_trie.substring(trie, 'b')
        assert not naive_suffix_trie.substring(trie, 'ab')

    def test_substring_multi_element_trie(self):
        """
        Tests substring operations on a multi-element trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('abba')
        expected = ['', 'a', 'ab', 'abb', 'abba', 'b', 'bb', 'bba', 'ba']
        unexpected = ['aba', 'aa', 'abbaa']
        for val in expected:
            assert naive_suffix_trie.substring(trie, val)
        for val in unexpected:
            assert not naive_suffix_trie.substring(trie, val)

            
class TestSuffix:

    def test_suffix_empty_trie(self):
        """
        Tests suffix operations on an empty trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('')
        assert naive_suffix_trie.suffix(trie, '')
        assert not naive_suffix_trie.suffix(trie, 'a')

    def test_suffix_single_element_trie(self):
        """
        Tests suffix operations on a single element trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('a')
        assert naive_suffix_trie.suffix(trie, '')
        assert naive_suffix_trie.suffix(trie, 'a')
        assert not naive_suffix_trie.suffix(trie, 'b')

    def test_suffix_multi_element_trie(self):
        """
        Tests suffix operations on a multi-element trie.
        """
        trie = naive_suffix_trie.build_suffix_trie('abba')
        expected = ['', 'a', 'ba', 'bba', 'abba']
        unexpected = ['ab', 'abb']
        for val in expected:
            assert naive_suffix_trie.suffix(trie, val)
        for val in unexpected:
            assert not naive_suffix_trie.suffix(trie, val)

