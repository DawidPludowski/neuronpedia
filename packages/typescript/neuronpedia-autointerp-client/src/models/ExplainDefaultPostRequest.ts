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
 * Request model for generating explanations of neuron/feature behavior
 * @export
 * @interface ExplainDefaultPostRequest
 */
export interface ExplainDefaultPostRequest {
    /**
     * List of activation records to analyze
     * @type {Array<NPActivation>}
     * @memberof ExplainDefaultPostRequest
     */
    activations: Array<NPActivation>;
    /**
     * API key for OpenRouter service
     * @type {string}
     * @memberof ExplainDefaultPostRequest
     */
    openrouterKey: string;
    /**
     * Model identifier to use for explanation generation
     * @type {string}
     * @memberof ExplainDefaultPostRequest
     */
    model: string;
}

/**
 * Check if a given object implements the ExplainDefaultPostRequest interface.
 */
export function instanceOfExplainDefaultPostRequest(value: object): value is ExplainDefaultPostRequest {
    if (!('activations' in value) || value['activations'] === undefined) return false;
    if (!('openrouterKey' in value) || value['openrouterKey'] === undefined) return false;
    if (!('model' in value) || value['model'] === undefined) return false;
    return true;
}

export function ExplainDefaultPostRequestFromJSON(json: any): ExplainDefaultPostRequest {
    return ExplainDefaultPostRequestFromJSONTyped(json, false);
}

export function ExplainDefaultPostRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ExplainDefaultPostRequest {
    if (json == null) {
        return json;
    }
    return {
        
        'activations': ((json['activations'] as Array<any>).map(NPActivationFromJSON)),
        'openrouterKey': json['openrouter_key'],
        'model': json['model'],
    };
}

export function ExplainDefaultPostRequestToJSON(json: any): ExplainDefaultPostRequest {
    return ExplainDefaultPostRequestToJSONTyped(json, false);
}

export function ExplainDefaultPostRequestToJSONTyped(value?: ExplainDefaultPostRequest | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'activations': ((value['activations'] as Array<any>).map(NPActivationToJSON)),
        'openrouter_key': value['openrouterKey'],
        'model': value['model'],
    };
}

