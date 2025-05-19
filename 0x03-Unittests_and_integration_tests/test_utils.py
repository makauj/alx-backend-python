#!/usr/bin/env python3
"""
the first unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
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

    def test_access_nested_map_exception(self):
        """
        Test access_nested_map function with exception
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map({"a": 1, "b": 2}, ("a", "b", "c"))
        with self.assertRaises(KeyError):
            utils.access_nested_map({"a": 1, "b": 2}, ("c",))

class TestGetJson(unittest.TestCase):
    """
    TestGetJson class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    def test_get_json(self, url, expected):
        """
        Test get_json function
        """
        config = {'return_value.json.return_value': expected}
        patcher = patch('requests.get', return_value=Mock(**config))
        mock_get = patcher.start()
        self.assertEqual(utils.get_json(url), expected)
        mock_get.assert_called_once_with(url)
        patcher.stop()

class TestMemoize(unittest.TestCase):
    """
    TestMemoize class that inherits from unittest.TestCase
    """
    def test_memoize(self):
        """
        Test memoize function
        """
        class TestClass:
            """
            TestClass class
            """
            def a_method(self):
                """
                a_method function
                """
                return 42
            
            @utils.memoize
            def a_property(self):
                """
                a_property function
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
