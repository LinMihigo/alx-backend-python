#!/usr/bin/env python3
"""Task 4
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """tests GithubOrgClient.org() function
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        GithubOrgClient(org_name).org
        mock_get_json.assert_called_once_with(expected_url)
