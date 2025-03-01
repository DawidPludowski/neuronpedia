# coding: utf-8

"""
    Neuronpedia - Inference Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1.0
    Contact: johnny@neuronpedia.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from neuronpedia_inference_client.models.steer_completion_chat_post200_response import SteerCompletionChatPost200Response

class TestSteerCompletionChatPost200Response(unittest.TestCase):
    """SteerCompletionChatPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SteerCompletionChatPost200Response:
        """Test SteerCompletionChatPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SteerCompletionChatPost200Response`
        """
        model = SteerCompletionChatPost200Response()
        if include_optional:
            return SteerCompletionChatPost200Response(
                outputs = [
                    neuronpedia_inference_client.models.np_steer_chat_result.NPSteerChatResult(
                        chat_template = [
                            neuronpedia_inference_client.models.np_steer_chat_message.NPSteerChatMessage(
                                content = '', 
                                role = '', )
                            ], 
                        raw = '', 
                        type = 'STEERED', )
                    ],
                input = neuronpedia_inference_client.models.np_steer_chat_result.NPSteerChatResult(
                    chat_template = [
                        neuronpedia_inference_client.models.np_steer_chat_message.NPSteerChatMessage(
                            content = '', 
                            role = '', )
                        ], 
                    raw = '', 
                    type = 'STEERED', )
            )
        else:
            return SteerCompletionChatPost200Response(
                outputs = [
                    neuronpedia_inference_client.models.np_steer_chat_result.NPSteerChatResult(
                        chat_template = [
                            neuronpedia_inference_client.models.np_steer_chat_message.NPSteerChatMessage(
                                content = '', 
                                role = '', )
                            ], 
                        raw = '', 
                        type = 'STEERED', )
                    ],
                input = neuronpedia_inference_client.models.np_steer_chat_result.NPSteerChatResult(
                    chat_template = [
                        neuronpedia_inference_client.models.np_steer_chat_message.NPSteerChatMessage(
                            content = '', 
                            role = '', )
                        ], 
                    raw = '', 
                    type = 'STEERED', ),
        )
        """

    def testSteerCompletionChatPost200Response(self):
        """Test SteerCompletionChatPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
