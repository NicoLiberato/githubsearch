import unittest
from unittest.mock import patch, MagicMock
import githubsearch

class TestGitHubSearch(unittest.TestCase):

    @patch('githubsearch.os.environ.get')
    @patch('githubsearch.getpass.getpass')
    def test_get_github_token_from_env(self, mock_getpass, mock_environ_get):
        mock_environ_get.return_value = 'fake_token'
        token = githubsearch.get_github_token()
        self.assertEqual(token, 'fake_token')
        mock_getpass.assert_not_called()

    @patch('githubsearch.os.environ.get')
    @patch('githubsearch.getpass.getpass')
    def test_get_github_token_from_input(self, mock_getpass, mock_environ_get):
        mock_environ_get.return_value = None
        mock_getpass.return_value = 'input_token'
        token = githubsearch.get_github_token()
        self.assertEqual(token, 'input_token')
        mock_getpass.assert_called_once()

    def test_print_curl_command(self):
        with patch('builtins.print') as mock_print:
            githubsearch.print_curl_command('GET', 'https://api.github.com/users/testuser', {'Authorization': 'token fake_token'})
            mock_print.assert_called_once_with("curl -X GET -H 'Authorization: token fake_token'  'https://api.github.com/users/testuser'")

    @patch('githubsearch.requests.get')
    def test_search_developer_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'login': 'testuser'}
        mock_get.return_value = mock_response

        result = githubsearch.search_developer('testuser')
        self.assertEqual(result, {'login': 'testuser'})

    @patch('githubsearch.requests.get')
    def test_search_developer_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = githubsearch.search_developer('nonexistentuser')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()