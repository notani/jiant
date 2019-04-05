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
