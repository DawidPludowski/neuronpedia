/* tslint:disable */
/* eslint-disable */
/**
 * Neuronpedia - Inference Server
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: johnny@neuronpedia.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface ActivationSinglePost200ResponseActivation
 */
export interface ActivationSinglePost200ResponseActivation {
    /**
     * 
     * @type {Array<number>}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    values: Array<number>;
    /**
     * 
     * @type {number}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    maxValue: number;
    /**
     * 
     * @type {number}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    maxValueIndex: number;
    /**
     * 
     * @type {Array<number>}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    dfaValues?: Array<number>;
    /**
     * 
     * @type {number}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    dfaMaxValue?: number;
    /**
     * 
     * @type {number}
     * @memberof ActivationSinglePost200ResponseActivation
     */
    dfaTargetIndex?: number;
}

/**
 * Check if a given object implements the ActivationSinglePost200ResponseActivation interface.
 */
export function instanceOfActivationSinglePost200ResponseActivation(value: object): value is ActivationSinglePost200ResponseActivation {
    if (!('values' in value) || value['values'] === undefined) return false;
    if (!('maxValue' in value) || value['maxValue'] === undefined) return false;
    if (!('maxValueIndex' in value) || value['maxValueIndex'] === undefined) return false;
    return true;
}

export function ActivationSinglePost200ResponseActivationFromJSON(json: any): ActivationSinglePost200ResponseActivation {
    return ActivationSinglePost200ResponseActivationFromJSONTyped(json, false);
}

export function ActivationSinglePost200ResponseActivationFromJSONTyped(json: any, ignoreDiscriminator: boolean): ActivationSinglePost200ResponseActivation {
    if (json == null) {
        return json;
    }
    return {
        
        'values': json['values'],
        'maxValue': json['max_value'],
        'maxValueIndex': json['max_value_index'],
        'dfaValues': json['dfa_values'] == null ? undefined : json['dfa_values'],
        'dfaMaxValue': json['dfa_max_value'] == null ? undefined : json['dfa_max_value'],
        'dfaTargetIndex': json['dfa_target_index'] == null ? undefined : json['dfa_target_index'],
    };
}

export function ActivationSinglePost200ResponseActivationToJSON(json: any): ActivationSinglePost200ResponseActivation {
    return ActivationSinglePost200ResponseActivationToJSONTyped(json, false);
}

export function ActivationSinglePost200ResponseActivationToJSONTyped(value?: ActivationSinglePost200ResponseActivation | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'values': value['values'],
        'max_value': value['maxValue'],
        'max_value_index': value['maxValueIndex'],
        'dfa_values': value['dfaValues'],
        'dfa_max_value': value['dfaMaxValue'],
        'dfa_target_index': value['dfaTargetIndex'],
    };
}

