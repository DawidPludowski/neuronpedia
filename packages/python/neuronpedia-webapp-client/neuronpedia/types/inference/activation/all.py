# generated by datamodel-codegen:
#   filename:  all.yaml

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class NPActivationAllActivation(BaseModel):
    source: str
    index: int
    values: List[float]
    sum_values: Optional[float] = None
    max_value: Optional[float] = None
    max_value_index: Optional[float] = None
    dfa_values: Optional[List[float]] = None
    dfa_target_index: Optional[int] = None
    dfa_max_value: Optional[float] = None


class NPActivationAllResponse(BaseModel):
    activations: Optional[List[NPActivationAllActivation]] = None
    tokens: Optional[List[str]] = None
    counts: Optional[List[List[float]]] = Field(
        None,
        description='Not currently supported and may be incorrect. This is the number of features that activated by layer, starting from layer 0 of this SAE. Need to be redesigned.',
    )


class NPActivationAllRequest(BaseModel):
    secret: str = Field(..., description='API secret for the inference server')
    prompt: str = Field(..., description='Input text prompt to get activations for')
    model: str = Field(..., description='Name of the model to test activations on')
    source_set: str = Field(..., description='The source set name of the SAEs (eg gemmascope-res-16k)')
    selected_sources: List[str] = Field(
        ...,
        description='List of specific SAEs to get activations for (eg ["0-gemmascope-res-65k", "5-gemmascope-res-65k"]). If not specified, will get activations for all SAEs in the source set.',
    )
    sort_by_token_indexes: List[int] = Field(
        ..., description='Sort the results by the sum of the activations at the specified token indexes.'
    )
    ignore_bos: bool = Field(
        ..., description='Whether or not to include features whose highest activation value is the BOS token.'
    )
    feature_filter: Optional[List[int]] = Field(
        None,
        description='Optional. If specified, will only return features that match the indexes specified. Can only be used if we\'re testing just one SAE ("selected_sources" length = 1).',
    )
    num_results: Optional[int] = Field(25, description='Optional. The number of top features to return.')
