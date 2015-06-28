from bot import *
import unittest2


class TestMedian(unittest2.TestCase):

    # testing for git repositories
    def testrepo(self):
        # download repo, folder should exist.
        grab_repo('DavidAwad', 'insightweets')
        self.assertEqual( True , os.path.isdir('local') )

        # remove .git, shouldn't still be there
        remove_git()
        self.assertEqual( False , os.path.isdir('local/.git') )

        # remove local dir, shouldn't still be there
        remove_local()
        self.assertEqual( False , os.path.isdir('local/.git') )
        self.assertEqual( False , os.path.isdir('local') )
        return


    def scrape_file(self):
        self.assertEquals(True ,process_repo())
        return

if __name__ == '__main__':
    unittest2.main()
