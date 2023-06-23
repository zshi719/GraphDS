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
        Check if all nodes' merge keys are included in the Constraints/Indexes
        """
        # Get all unique property names from the constraints

        constraint_properties = []
        for constraint in CONSTRAINTS:
            matches = re.findall(r'FOR \((.*?):', constraint)
            constraint_properties += matches

        # Get all label names from the nodes
        node_labels = []
        for node in NODES:
            labels = node['labels']
            labels = [label for label in labels if label not in ('Sourcescrub', 'Crunchbase')]
            node_labels += labels

        for label in node_labels:
            self.assertIn(label, constraint_properties,
                          msg=f"Missing constraint for label {label}")


validate_obj = ValidateModel()
# validate_obj.test_missing_fields()
validate_obj.test_constraints_completeness()

# %%
