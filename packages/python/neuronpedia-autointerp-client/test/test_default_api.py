# coding: utf-8

"""
    Neuronpedia - AutoInterp Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: johnny@neuronpedia.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from neuronpedia_autointerp_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_explain_default_post(self) -> None:
        """Test case for explain_default_post

        Generate an explanation for neuron/feature behavior using the default explainer
        """
        pass

    def test_score_embedding_post(self) -> None:
        """Test case for score_embedding_post

        Score an explanation using embedding similarity, using the dunzhang/stella_en_400M_v5 model.
        """
        pass

    def test_score_fuzz_detection_post(self) -> None:
        """Test case for score_fuzz_detection_post

        Score an explanation using fuzzing or detection methods
        """
        pass


if __name__ == '__main__':
    unittest.main()
