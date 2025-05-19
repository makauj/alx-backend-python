#!/usr/bin/env python3
"""
the first unit test for utils.access_nested_map
"""
from unittest import TestCase
from parameterized import parameterized
import utils


class TestAccessNestedMap(TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        (
            {"a": 1, "b": 2, "c": 3},
            ("a",),
            1,
        ),
        (
            {"a": 1, "b": 2, "c": 3},
            ("b",),
            2,
        ),
        (
            {"a": 1, "b": 2, "c": 3},
            ("c",),
            3,
        ),
        (
            {"a": {"b": 2}},
            ("a", "b"),
            2,
        ),
        (
            {"a": {"b": {"c": 3}}},
            ("a", "b", "c"),
            3,
        ),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
