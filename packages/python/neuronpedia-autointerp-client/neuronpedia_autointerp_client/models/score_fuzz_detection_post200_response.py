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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from neuronpedia_autointerp_client.models.score_fuzz_detection_post200_response_breakdown_inner import ScoreFuzzDetectionPost200ResponseBreakdownInner
from typing import Optional, Set
from typing_extensions import Self

class ScoreFuzzDetectionPost200Response(BaseModel):
    """
    ScoreFuzzDetectionPost200Response
    """ # noqa: E501
    score: Union[StrictFloat, StrictInt] = Field(description="The score from 0 to 1")
    breakdown: List[ScoreFuzzDetectionPost200ResponseBreakdownInner]
    __properties: ClassVar[List[str]] = ["score", "breakdown"]

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
        """Create an instance of ScoreFuzzDetectionPost200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in breakdown (list)
        _items = []
        if self.breakdown:
            for _item_breakdown in self.breakdown:
                if _item_breakdown:
                    _items.append(_item_breakdown.to_dict())
            _dict['breakdown'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScoreFuzzDetectionPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "score": obj.get("score"),
            "breakdown": [ScoreFuzzDetectionPost200ResponseBreakdownInner.from_dict(_item) for _item in obj["breakdown"]] if obj.get("breakdown") is not None else None
        })
        return _obj


