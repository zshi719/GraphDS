from data_model.nodes import NODES
from data_model.relationships import RELATIONSHIPS
from data_model.constraints import CONSTRAINTS
import unittest
import re


class ValidateModel(unittest.TestCase):
    def test_missing_fields(self):
        """
        Check if all the field names in the data model are present in the csv files and/or the tables
        :return:
        """

        # self.assertEqual("", 4, f"Failed msg")
        pass

    def test_constraints_completeness(self):
        """
        Check if all nodes' merge keys and all relationships' start/end nodes are included in the Constraints/Indexes
        :return:
        """


validate_obj = ValidateModel()
validate_obj.test_missing_fields()
validate_obj.test_constraints_completeness()
