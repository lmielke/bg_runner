# test_runner.py

import logging
import os
import unittest
import yaml

from runner.runner import DefaultClass
import runner.settings as sts


class Test_DefaultClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verbose = 0
        cls.testData = cls.mk_test_data()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def mk_test_data(cls):
        with open(os.path.join(sts.test_data_dir, "test_runner.yml"), "r") as f:
            return yaml.safe_load(f)

    def test___str__(self):
        pc = DefaultClass(pg_name="runner", py_version="3.7")
        expected = "DefaultClass: runner"
        self.assertEqual(str(pc), expected)
        logging.info("Info level log from the test")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
