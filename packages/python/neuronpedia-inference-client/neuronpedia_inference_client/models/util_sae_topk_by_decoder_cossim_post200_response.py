# coding: utf-8

"""
    Neuronpedia - Inference Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1.0
    Contact: johnny@neuronpedia.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from neuronpedia_inference_client.models.np_feature import NPFeature
from neuronpedia_inference_client.models.util_sae_topk_by_decoder_cossim_post200_response_topk_decoder_cossim_features_inner import UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner
from typing import Optional, Set
from typing_extensions import Self

class UtilSaeTopkByDecoderCossimPost200Response(BaseModel):
    """
    UtilSaeTopkByDecoderCossimPost200Response
    """ # noqa: E501
    feature: Optional[NPFeature] = None
    topk_decoder_cossim_features: Optional[List[UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner]] = None
    __properties: ClassVar[List[str]] = ["feature", "topk_decoder_cossim_features"]

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
        """Create an instance of UtilSaeTopkByDecoderCossimPost200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of feature
        if self.feature:
            _dict['feature'] = self.feature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in topk_decoder_cossim_features (list)
        _items = []
        if self.topk_decoder_cossim_features:
            for _item_topk_decoder_cossim_features in self.topk_decoder_cossim_features:
                if _item_topk_decoder_cossim_features:
                    _items.append(_item_topk_decoder_cossim_features.to_dict())
            _dict['topk_decoder_cossim_features'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UtilSaeTopkByDecoderCossimPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feature": NPFeature.from_dict(obj["feature"]) if obj.get("feature") is not None else None,
            "topk_decoder_cossim_features": [UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner.from_dict(_item) for _item in obj["topk_decoder_cossim_features"]] if obj.get("topk_decoder_cossim_features") is not None else None
        })
        return _obj


