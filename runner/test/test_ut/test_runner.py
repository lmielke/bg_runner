# test_runner.py
# C:\Users\lars\python_venvs\packages\bg_runner\runner\test\test_ut\test_runner.py

import logging
import os
import unittest
import yaml

from runner.runner import DefaultClass
from runner.helpers.function_to_json import FunctionToJson
import runner.settings as sts


class Test_DefaultClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verbose = 0

    @classmethod
    def tearDownClass(cls):
        pass

    @FunctionToJson(schemas={"openai"}, write=True)
    def test___str__(self):
        pc = DefaultClass(pr_name="bg_runner", pg_name="runner", py_version="3.7")
        expected = "DefaultClass: self.pg_name = 'runner'"
        self.assertEqual(str(pc), expected)
        logging.info("Info level log from the test")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
