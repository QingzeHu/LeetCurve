import unittest
from data.github_api import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.github = GitHubAPI("QingzeHu/Leetcode")

    def test_get_files(self):
        files = self.github.get_files()
        self.assertIsInstance(files, list)

    def test_get_commits(self):
        commits = self.github.get_commits("path/to/a/file.go")
        self.assertIsInstance(commits, list)

if __name__ == '__main__':
    unittest.main()
