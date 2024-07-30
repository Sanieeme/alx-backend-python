#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """method that test"""
        expected_response = {"mock": "data"}
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(result, expected_response)

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos")
    ])
    @patch('client.get_json')
    def test_public_repos_url(self, org_name, expected_url, mock_get_json):
        mock_get_json.return_value = {"repos_url": expected_url}

        client = GithubOrgClient(org_name)

        self.assertEqual(client._public_repos_url, expected_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Parametrize the test """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


if __name__ == '__main__':
    unittest.main()
