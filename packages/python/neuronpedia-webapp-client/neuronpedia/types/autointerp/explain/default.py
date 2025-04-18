# generated by datamodel-codegen:
#   filename:  default.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class NPActivation(BaseModel):
    tokens: List[str] = Field(..., description='List of tokens for this text', example=['The', 'cat', 'sat'])
    values: List[float] = Field(
        ..., description='Activation values corresponding to each token', example=[0.5, 0.8, 0.2]
    )


class NPExplainDefaultResponse(BaseModel):
    explanation: str = Field(..., description='The generated explanation for the given set of activations')


class NPExplainDefaultRequest(BaseModel):
    activations: List[NPActivation] = Field(..., description='List of activation records to analyze')
    openrouter_key: str = Field(..., description='API key for OpenRouter service', example='sk-or-v1-...')
    model: str = Field(
        ..., description='Model identifier to use for explanation generation', example='openai/gpt-4o-mini'
    )
    secret: str = Field(..., description='Authentication secret for the API', example='your-secret-key')
