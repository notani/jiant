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
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, cuda = 2"

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

# jSAA

```shell
source my_path_config.sh; python main.py --config_file config/jSAA.conf --overrides "exp_name = exp/ja/SAA/ipadic, run_name = 0, word_embs_file = vectors/ja/GloVe/ipadic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = ipadic, jsaa_domain = books, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAA.conf --overrides "exp_name = exp/ja/SAA/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, jsaa_domain = books, cuda = 0"

source my_path_config.sh; python main.py --config_file config/jSAA.conf --overrides "exp_name = exp/ja/SAA/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, jsaa_domain = books, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAA.conf --overrides "exp_name = exp/ja/SAA/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, jsaa_domain = books, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAA.conf --overrides "exp_name = exp/ja/SAA/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, jsaa_domain = books, cuda = 0"
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
Max: 137, Min: 2
Mean: 19.85896467031929, Std: 15.633400622539677
Percentile[25, 50, 75]: [ 9. 14. 27.]

## ipadic
Max: 126, Min: 2
Mean: 18.51294162100888, Std: 14.130069472930266
Percentile[25, 50, 75]: [ 8. 14. 25.]

## spm
Max: 144, Min: 4
Mean: 22.00443982618553, Std: 16.265093242959594
Percentile[25, 50, 75]: [10.   16.   29.75]

Max: 124, Min: 3
Mean: 19.193840921972416, Std: 14.000574326389005
Percentile[25, 50, 75]: [ 9. 14. 25.]

Max: 112, Min: 3
Mean: 17.14670319289628, Std: 12.485121203202851
Percentile[25, 50, 75]: [ 8. 13. 23.]
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
Max: 34, Min: 5
Mean: 12.632947198275861, Std: 4.58646547569171
Percentile[25, 50, 75]: [ 9. 12. 15.]

## ipadic
Max: 34, Min: 5
Mean: 12.135102370689655, Std: 4.258350890465767
Percentile[25, 50, 75]: [ 9. 11. 15.]

## spm
Max: 43, Min: 6
Mean: 14.625404094827585, Std: 5.022782803273753
Percentile[25, 50, 75]: [11. 14. 18.]

Max: 37, Min: 5
Mean: 12.785425646551724, Std: 4.09503193035602
Percentile[25, 50, 75]: [10. 12. 15.]

Max: 34, Min: 4
Mean: 11.322467672413794, Std: 3.5791920727101916
Percentile[25, 50, 75]: [ 9. 11. 13.]
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
Max: 61, Min: 1
Mean: 13.222715514227785, Std: 6.713874119550587
Percentile[25, 50, 75]: [ 8. 12. 17.]

## ipadic
Max: 56, Min: 1
Mean: 12.759106481157799, Std: 6.4151156738313455
Percentile[25, 50, 75]: [ 8. 12. 16.]

## spm
Max: 67, Min: 1
Mean: 15.66875830245403, Std: 7.43903140587066
Percentile[25, 50, 75]: [10. 14. 20.]

Max: 57, Min: 1
Mean: 13.60506537090121, Std: 6.491419551403433
Percentile[25, 50, 75]: [ 9. 13. 17.]

Max: 53, Min: 1
Mean: 12.177515206600013, Std: 5.8100769581200264
Percentile[25, 50, 75]: [ 8. 11. 15.]
```


## SAA (sentiment analysis amazon)

### Books

`data/ja/SAA/books`

```shell

# train.tsv: 1600
    807 0
    793 1

# dev.tsv: 400
    193 0
    207 1
      
# test.tsv: 2000
   1000 0
   1000 1

# Text length (# of tokens)
python scripts/calc_avg_length.py data/ja/SAA/books/unidic/
python scripts/calc_avg_length.py data/ja/SAA/books/ipadic/
python scripts/calc_avg_length.py data/ja/SAA/books/spm/8000
python scripts/calc_avg_length.py data/ja/SAA/books/spm/16000
python scripts/calc_avg_length.py data/ja/SAA/books/spm/32000


Text: 4000

## unidic
Max: 2163, Min: 4
Mean: 164.554, Std: 125.89941653558209
Percentile[25, 50, 75]: [ 84. 130. 210.]

## ipadic
Max: 1875, Min: 4
Mean: 157.63725, Std: 118.7681719251311
Percentile[25, 50, 75]: [ 80.  125.5 201. ]

## spm
Max: 2748, Min: 4
Mean: 180.58575, Std: 138.68836521834663
Percentile[25, 50, 75]: [ 93. 144. 228.]

Max: 2433, Min: 3
Mean: 156.57825, Std: 120.89711897699424
Percentile[25, 50, 75]: [ 81. 125. 197.]

Max: 2173, Min: 3
Mean: 140.1215, Std: 108.3927291738242
Percentile[25, 50, 75]: [ 72. 111. 177.]
```

### DVD

`data/ja/SAA/dvd`

```shell

# train.tsv: 1600
    810 0
    790 1

# dev.tsv: 400
    190 0
    210 1
      
# test.tsv: 2000
   1000 0
   1000 1

# Text length (# of tokens)
python scripts/calc_avg_length.py data/ja/SAA/dvd/unidic/
python scripts/calc_avg_length.py data/ja/SAA/dvd/ipadic/
python scripts/calc_avg_length.py data/ja/SAA/dvd/spm/8000
python scripts/calc_avg_length.py data/ja/SAA/dvd/spm/16000
python scripts/calc_avg_length.py data/ja/SAA/dvd/spm/32000


Text: 4000

## unidic
Max: 2196, Min: 5
Mean: 159.53925, Std: 121.88970202374563
Percentile[25, 50, 75]: [ 79. 126. 208.]

## ipadic
Max: 2080, Min: 5
Mean: 152.2935, Std: 115.8189097589422
Percentile[25, 50, 75]: [ 75.   120.   197.25]

## spm
Max: 2317, Min: 11
Mean: 181.68, Std: 137.49596030429404
Percentile[25, 50, 75]: [ 90. 144. 235.]

Max: 2046, Min: 10
Mean: 157.4715, Std: 119.89147045453234
Percentile[25, 50, 75]: [ 78. 124. 203.]

Max: 1810, Min: 9
Mean: 140.94175, Std: 107.5998181082919
Percentile[25, 50, 75]: [ 70. 111. 181.]
```

### Music

`data/ja/SAA/music`

```shell

# train.tsv: 1600
    790 0
    810 1

# dev.tsv: 400
    210 0
    190 1
      
# test.tsv: 2000
   1000 0
   1000 1

# Text length (# of tokens)
python scripts/calc_avg_length.py data/ja/SAA/music/unidic/
python scripts/calc_avg_length.py data/ja/SAA/music/ipadic/
python scripts/calc_avg_length.py data/ja/SAA/music/spm/8000
python scripts/calc_avg_length.py data/ja/SAA/music/spm/16000
python scripts/calc_avg_length.py data/ja/SAA/music/spm/32000


Text: 4000

## unidic
Max: 1042, Min: 8
Mean: 138.90975, Std: 104.72254105462443
Percentile[25, 50, 75]: [ 69.  108.5 179. ]

## ipadic
Max: 995, Min: 8
Mean: 130.50075, Std: 98.20354881284841
Percentile[25, 50, 75]: [ 65.   102.   168.25]

## spm
Max: 1114, Min: 9
Mean: 160.08275, Std: 118.74927537647335
Percentile[25, 50, 75]: [ 81. 126. 205.]

Max: 1004, Min: 9
Mean: 138.765, Std: 103.02367579833289
Percentile[25, 50, 75]: [ 70.   109.   178.25]

Max: 896, Min: 7
Mean: 123.83325, Std: 91.7905193603212
Percentile[25, 50, 75]: [ 63.   97.5 159. ]
```
