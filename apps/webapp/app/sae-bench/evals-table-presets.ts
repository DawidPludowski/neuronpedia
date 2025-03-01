/* eslint-disable import/no-cycle */
import { EvalsTableParams } from './evals-table';

export const EVALS_TABLE_PRESETS: { name: string; params: EvalsTableParams }[] = [
  {
    name: 'Absorption',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'absorption_first_letter||mean||mean_absorption_fraction_score',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'Core',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'core||model_performance_preservation||ce_loss_score',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'SCR',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'scr||scr_metrics||scr_metric_threshold_20',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'TPP',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'tpp||tpp_metrics||tpp_threshold_20_total_metric',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'Unlearning',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'unlearning||unlearning||unlearning_score',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'Sparse Probing',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'sparse_probing||sae||sae_top_1_test_accuracy',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
  {
    name: 'AutoInterp',
    params: {
      metricX: 'core||sparsity||l0',
      metricY: 'autointerp||autointerp||autointerp_score',
      logX: true,
      logY: false,
      groupBy: 'saeClass',
      modelFilter: ['gemma-2-2b'],
      releaseFilter: ['sae_bench_0125'],
      saeClassFilter: [],
      widthFilter: [65536],
      layerFilter: [12],
      trainingTokensFilter: [499998720],
    },
  },
];
