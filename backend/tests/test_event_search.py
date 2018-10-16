from unittest import TestCase
from app.event_search import convert_root_to_dict, convert_search_terms_to_xquery, search_by_xquery
from lxml import etree as ET
from tests import TEST_EVENTS_ROOT
from glob import glob


class TestEventSearch(TestCase):
    def test_convert_root_to_dict(self):
        for filename in glob(TEST_EVENTS_ROOT + "/*single.xml"):
            print(filename)
            answer = filename.replace(".xml", "_answer")
            with open(answer, "r") as afile:
                tree = ET.parse(filename)
                root = tree.xpath("./parameter")[0]
                self.assertEqual(str(convert_root_to_dict(root)), afile.read())

    def test_convert_search_terms_to_xquery(self):
        one_level_one_parameter = dict(country='NED')
        one_level_one_parameter_answer = "//root/parameter[.//parameter[@name='country' and text()='NED']]"

        self.assertEqual(one_level_one_parameter_answer, convert_search_terms_to_xquery(one_level_one_parameter))

        one_level_two_parameters = dict(country='NED', months=123)
        one_level_two_parameters_answer = "//root/parameter[.//parameter[@name='country' and text()='NED']][" \
                                          ".//parameter[@name='months' and number()=123]]"

        self.assertEqual(one_level_two_parameters_answer, convert_search_terms_to_xquery(one_level_two_parameters))

        two_level_one_parameter = dict(trigger=dict(has_dlc='Third Rome'))
        two_level_one_parameter_answer = "//root/parameter[.//parameter[@name='trigger']//parameter[@name='has_dlc' " \
                                         "and text()='Third Rome']]"
        self.assertEqual(two_level_one_parameter_answer, convert_search_terms_to_xquery(two_level_one_parameter))

        two_level_two_parameter = dict(trigger=dict(has_dlc='Third Rome'), tag='NED')
        two_level_two_parameter_answer = "//root/parameter[.//parameter[@name='trigger']//parameter[@name='has_dlc' " \
                                         "and text()='Third Rome']][.//parameter[@name='tag' and text()='NED']]"

        self.assertEqual(two_level_two_parameter_answer, convert_search_terms_to_xquery(two_level_two_parameter))

    def test_search_by_xquery(self):
        ned_123_mtth = search_by_xquery("//root/parameter[.//parameter[text()='HOL']][.//parameter[@name='months' and "
                                        "number()=123]]")
        self.assertEqual(ned_123_mtth[0].xpath("./parameter[@name='id']")[0].text, "flavor_hol.5120")