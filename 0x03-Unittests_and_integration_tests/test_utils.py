#!/usr/bin/env python3
"""import modusle """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """method """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, exception: type) -> None:
        """ Use the assertRaises context manager to test
        that a KeyError is raised
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock) -> None:
        """test json"""
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response

        results = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(results, test_payload)


if __name__ == '__main__':
    unittest.main()
