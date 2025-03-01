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

from neuronpedia_autointerp_client.models.score_fuzz_detection_post_request import ScoreFuzzDetectionPostRequest

class TestScoreFuzzDetectionPostRequest(unittest.TestCase):
    """ScoreFuzzDetectionPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScoreFuzzDetectionPostRequest:
        """Test ScoreFuzzDetectionPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScoreFuzzDetectionPostRequest`
        """
        model = ScoreFuzzDetectionPostRequest()
        if include_optional:
            return ScoreFuzzDetectionPostRequest(
                activations = [
                    neuronpedia_autointerp_client.models.np_activation.NPActivation(
                        tokens = ["The","cat","sat"], 
                        values = [0.5,0.8,0.2], )
                    ],
                explanation = 'This neuron activates on references to feline behavior',
                openrouter_key = 'sk-or-v1-...',
                model = 'openai/gpt-4o-mini',
                type = 'FUZZ'
            )
        else:
            return ScoreFuzzDetectionPostRequest(
                activations = [
                    neuronpedia_autointerp_client.models.np_activation.NPActivation(
                        tokens = ["The","cat","sat"], 
                        values = [0.5,0.8,0.2], )
                    ],
                explanation = 'This neuron activates on references to feline behavior',
                openrouter_key = 'sk-or-v1-...',
                model = 'openai/gpt-4o-mini',
                type = 'FUZZ',
        )
        """

    def testScoreFuzzDetectionPostRequest(self):
        """Test ScoreFuzzDetectionPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
