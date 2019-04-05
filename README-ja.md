# Preparation

1. Download word embeddings and update file paths in `up my_path_config.sh`.
2. Update `project_dir` and `global_ro_exp_dir` in `config/j*.conf`.

```
// write to local storage by default for this demo
project_dir = <path to the project dir>
exp_name = jiant-demo
run_name = ja-demo
global_ro_exp_dir = <path to the experiment dir>
```

# jRTE

```shell
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/ipadic, run_name = 0, word_embs_file = vectors/ja/GloVe/ipadic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = ipadic, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, cuda = 0"

source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, cuda = 0"
```

# jWNLI

```shell
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/ipadic, run_name = 0, word_embs_file = vectors/ja/GloVe/ipadic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = ipadic, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, cuda = 0"

source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, cuda = 0"
```

# jDP

```shell
source my_path_config.sh; python main.py --config_file config/jDP.conf --overrides "exp_name = exp/ja/DP/ipadic, run_name = 0, word_embs_file = vectors/ja/GloVe/ipadic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = ipadic, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jDP.conf --overrides "exp_name = exp/ja/DP/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, cuda = 0"

source my_path_config.sh; python main.py --config_file config/jDP.conf --overrides "exp_name = exp/ja/DP/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jDP.conf --overrides "exp_name = exp/ja/DP/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jDP.conf --overrides "exp_name = exp/ja/DP/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, cuda = 0"
```

# Data Statistics

## RTE

`data/ja/RTE`

```
# train.tsv: 3793
   2234 entailment
   1559 not_entailment
   
# dev.tsv: 500
    279 entailment
    221 not_entailment

# test.tsv: 1000
    579 entailment
    421 not_entailment
    
    
# Text length (# of tokens)

python scripts/calc_avg_length.py data/ja/RTE/unidic/
python scripts/calc_avg_length.py data/ja/RTE/ipadic/
python scripts/calc_avg_length.py data/ja/RTE/spm/8000
python scripts/calc_avg_length.py data/ja/RTE/spm/16000
python scripts/calc_avg_length.py data/ja/RTE/spm/32000

Text: 10586

## unidic
Max: 355, Min: 5
Mean: 52.25552616663518, Std: 41.296737603836526
Percentile[25, 50, 75]: [22. 38. 72.]

## ipadic
Max: 342, Min: 5
Mean: 50.90950311732477, Std: 39.718872406446785
Percentile[25, 50, 75]: [21. 37. 70.]

## spm
Max: 359, Min: 7
Mean: 54.468921216701304, Std: 42.08559902725326
Percentile[25, 50, 75]: [23. 40. 75.]

Max: 339, Min: 7
Mean: 51.658322312488195, Std: 39.766346139216246
Percentile[25, 50, 75]: [22. 38. 71.]

Max: 328, Min: 7
Mean: 49.611184583412054, Std: 38.228073051336736
Percentile[25, 50, 75]: [21. 36. 68.]
```

## WNLI

`data/ja/WNLI`

```
# train.tsv: 2040
   1020 1
   1020 0
   
# dev.tsv: 658
    284 1
    284 0
    
# test.tsv: 1104
    552 1
    552 0
    
# Text length (# of tokens)

python scripts/calc_avg_length.py data/ja/WNLI/unidic/
python scripts/calc_avg_length.py data/ja/WNLI/ipadic/
python scripts/calc_avg_length.py data/ja/WNLI/spm/8000
python scripts/calc_avg_length.py data/ja/WNLI/spm/16000
python scripts/calc_avg_length.py data/ja/WNLI/spm/32000

Text: 7424

## unidic
Max: 96, Min: 13
Mean: 34.43790409482759, Std: 12.89349072789386
Percentile[25, 50, 75]: [24. 32. 42.]

## ipadic
Max: 92, Min: 13
Mean: 33.94005926724138, Std: 12.461613074860008
Percentile[25, 50, 75]: [24. 31. 42.]

## spm
Max: 110, Min: 14
Mean: 36.423626077586206, Std: 13.357519070952948
Percentile[25, 50, 75]: [26. 34. 45.]

Max: 104, Min: 14
Mean: 34.58364762931034, Std: 12.363435333535923
Percentile[25, 50, 75]: [25. 32. 42.]

Max: 101, Min: 13
Mean: 33.12068965517241, Std: 11.855564074491594
Percentile[25, 50, 75]: [24. 31. 40.]
```

## DP

`data/ja/DP`

```
# train.tsv: 34548
  33626 other
    448 cause/reason
    206 condition
     99 contrast
     98 purpose
     54 ground
     17 concession

# dev.tsv: 11314
  11014 other
    158 cause/reason
     60 condition
     43 purpose
     21 contrast
     12 ground
      6 concession
      
# test.tsv: 11350
  11057 other
    131 cause/reason
     67 condition
     40 purpose
     34 contrast
     13 ground
      8 concession
      
# Text length (# of tokens)

python scripts/calc_avg_length.py data/ja/DP/unidic/
python scripts/calc_avg_length.py data/ja/DP/ipadic/
python scripts/calc_avg_length.py data/ja/DP/spm/8000
python scripts/calc_avg_length.py data/ja/DP/spm/16000
python scripts/calc_avg_length.py data/ja/DP/spm/32000

Text: 114424

## unidic
Max: 145, Min: 2
Mean: 35.066087534083756, Std: 17.625382639141353
Percentile[25, 50, 75]: [22. 32. 45.]

## ipadic
Text: 114424
Max: 140, Min: 2
Mean: 34.60247850101377, Std: 17.29617680569224

## spm
Max: 156, Min: 3
Mean: 37.51599314829057, Std: 18.3348060154627
Percentile[25, 50, 75]: [24. 34. 48.]

Max: 147, Min: 3
Mean: 35.45230021673775, Std: 17.333206916280027
Percentile[25, 50, 75]: [23. 33. 45.]

Max: 140, Min: 3
Mean: 34.02475005243655, Std: 16.646029929556107
Percentile[25, 50, 75]: [22. 31. 43.]
```
