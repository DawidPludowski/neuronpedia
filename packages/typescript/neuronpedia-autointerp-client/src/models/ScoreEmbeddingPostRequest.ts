/* tslint:disable */
/* eslint-disable */
/**
 * Neuronpedia - AutoInterp Server
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: johnny@neuronpedia.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { NPActivation } from './NPActivation';
import {
    NPActivationFromJSON,
    NPActivationFromJSONTyped,
    NPActivationToJSON,
    NPActivationToJSONTyped,
} from './NPActivation';

/**
 * Request model for scoring explanations using embedding similarity
 * @export
 * @interface ScoreEmbeddingPostRequest
 */
export interface ScoreEmbeddingPostRequest {
    /**
     * List of activation records to analyze
     * @type {Array<NPActivation>}
     * @memberof ScoreEmbeddingPostRequest
     */
    activations: Array<NPActivation>;
    /**
     * The explanation to evaluate
     * @type {string}
     * @memberof ScoreEmbeddingPostRequest
     */
    explanation: string;
}

/**
 * Check if a given object implements the ScoreEmbeddingPostRequest interface.
 */
export function instanceOfScoreEmbeddingPostRequest(value: object): value is ScoreEmbeddingPostRequest {
    if (!('activations' in value) || value['activations'] === undefined) return false;
    if (!('explanation' in value) || value['explanation'] === undefined) return false;
    return true;
}

export function ScoreEmbeddingPostRequestFromJSON(json: any): ScoreEmbeddingPostRequest {
    return ScoreEmbeddingPostRequestFromJSONTyped(json, false);
}

export function ScoreEmbeddingPostRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ScoreEmbeddingPostRequest {
    if (json == null) {
        return json;
    }
    return {
        
        'activations': ((json['activations'] as Array<any>).map(NPActivationFromJSON)),
        'explanation': json['explanation'],
    };
}

export function ScoreEmbeddingPostRequestToJSON(json: any): ScoreEmbeddingPostRequest {
    return ScoreEmbeddingPostRequestToJSONTyped(json, false);
}

export function ScoreEmbeddingPostRequestToJSONTyped(value?: ScoreEmbeddingPostRequest | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'activations': ((value['activations'] as Array<any>).map(NPActivationToJSON)),
        'explanation': value['explanation'],
    };
}

