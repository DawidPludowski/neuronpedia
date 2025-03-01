# coding: utf-8

"""
    Neuronpedia - AutoInterp Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: johnny@neuronpedia.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ScoreFuzzDetectionPost200ResponseBreakdownInner(BaseModel):
    """
    The \"scorer.__call__\" result's score breakdown. Type copied from https://github.com/EleutherAI/sae-auto-interp/blob/3659ff3bfefbe2628d37484e5bcc0087a5b10a27/sae_auto_interp/scorers/classifier/sample.py#L19
    """ # noqa: E501
    str_tokens: Optional[List[StrictStr]] = Field(default=None, description="List of strings")
    activations: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="List of floats")
    distance: Optional[StrictInt] = Field(default=None, description="Quantile or neighbor distance")
    ground_truth: Optional[StrictBool] = Field(default=None, description="Whether the example is activating or not")
    prediction: Optional[StrictBool] = Field(default=False, description="Whether the model predicted the example activating or not")
    highlighted: Optional[StrictBool] = Field(default=False, description="Whether the sample is highlighted")
    probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.0, description="The probability of the example activating")
    correct: Optional[StrictBool] = Field(default=False, description="Whether the prediction is correct")
    __properties: ClassVar[List[str]] = ["str_tokens", "activations", "distance", "ground_truth", "prediction", "highlighted", "probability", "correct"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScoreFuzzDetectionPost200ResponseBreakdownInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScoreFuzzDetectionPost200ResponseBreakdownInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "str_tokens": obj.get("str_tokens"),
            "activations": obj.get("activations"),
            "distance": obj.get("distance"),
            "ground_truth": obj.get("ground_truth"),
            "prediction": obj.get("prediction") if obj.get("prediction") is not None else False,
            "highlighted": obj.get("highlighted") if obj.get("highlighted") is not None else False,
            "probability": obj.get("probability") if obj.get("probability") is not None else 0.0,
            "correct": obj.get("correct") if obj.get("correct") is not None else False
        })
        return _obj


