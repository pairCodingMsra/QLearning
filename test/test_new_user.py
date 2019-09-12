from unittest import TestCase
import api


class TestNew_user(TestCase):

    def test_new_user(self):
        if not api.new_user("huangzp"):
            self.fail()
