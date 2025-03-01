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
/**
 * The "scorer.__call__" result's score breakdown. With exception of fixing similarity to change to number instead of array of number, type is copied from https://github.com/EleutherAI/sae-auto-interp/blob/3659ff3bfefbe2628d37484e5bcc0087a5b10a27/sae_auto_interp/scorers/embedding/embedding.py#L20
 * @export
 * @interface ScoreEmbeddingPost200ResponseBreakdownInner
 */
export interface ScoreEmbeddingPost200ResponseBreakdownInner {
    /**
     * The text that was used to evaluate the similarity
     * @type {string}
     * @memberof ScoreEmbeddingPost200ResponseBreakdownInner
     */
    text: string;
    /**
     * Quantile or neighbor distance
     * @type {number}
     * @memberof ScoreEmbeddingPost200ResponseBreakdownInner
     */
    distance: number;
    /**
     * What is the similarity of the example to the explanation
     * @type {number}
     * @memberof ScoreEmbeddingPost200ResponseBreakdownInner
     */
    similarity: number;
}

/**
 * Check if a given object implements the ScoreEmbeddingPost200ResponseBreakdownInner interface.
 */
export function instanceOfScoreEmbeddingPost200ResponseBreakdownInner(value: object): value is ScoreEmbeddingPost200ResponseBreakdownInner {
    if (!('text' in value) || value['text'] === undefined) return false;
    if (!('distance' in value) || value['distance'] === undefined) return false;
    if (!('similarity' in value) || value['similarity'] === undefined) return false;
    return true;
}

export function ScoreEmbeddingPost200ResponseBreakdownInnerFromJSON(json: any): ScoreEmbeddingPost200ResponseBreakdownInner {
    return ScoreEmbeddingPost200ResponseBreakdownInnerFromJSONTyped(json, false);
}

export function ScoreEmbeddingPost200ResponseBreakdownInnerFromJSONTyped(json: any, ignoreDiscriminator: boolean): ScoreEmbeddingPost200ResponseBreakdownInner {
    if (json == null) {
        return json;
    }
    return {
        
        'text': json['text'],
        'distance': json['distance'],
        'similarity': json['similarity'],
    };
}

export function ScoreEmbeddingPost200ResponseBreakdownInnerToJSON(json: any): ScoreEmbeddingPost200ResponseBreakdownInner {
    return ScoreEmbeddingPost200ResponseBreakdownInnerToJSONTyped(json, false);
}

export function ScoreEmbeddingPost200ResponseBreakdownInnerToJSONTyped(value?: ScoreEmbeddingPost200ResponseBreakdownInner | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'text': value['text'],
        'distance': value['distance'],
        'similarity': value['similarity'],
    };
}

