import pytest
from unittest import TestCase
import api


class TestNew_user(TestCase):

    def test_new_user(self):
        self.assertIsNotNone(api.new_user("huangzp"))


