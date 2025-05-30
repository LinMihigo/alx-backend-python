#!/usr/bin/env python3
"""Task 0 to 2
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import memoize
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """The get_json function tests
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """tests utils.get_json()
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch(
            'utils.requests.get',
            return_value=mock_response
                ) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests
    """
    def test_memoize(self):
        """tests utils.memoize()
        """
        class TestClass:
            """docs
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """docs
                """
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
                ) as mock_method:
            """docs
            """
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
