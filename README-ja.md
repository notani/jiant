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
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, cuda = 0"
```

# jWNLI

```shell
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jWNLI.conf --overrides "exp_name = exp/ja/WNLI/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, cuda = 0"
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
```
