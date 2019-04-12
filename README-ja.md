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
source my_path_config.sh; python main.py --config_file config/jRTE.conf --overrides "exp_name = exp/ja/RTE/jumanpp, run_name = 0, word_embs_file = vectors/ja/GloVe/jumanpp/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = jumanpp, cuda = 2"

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

# jSAR

```shell
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/ipadic, run_name = 0, word_embs_file = vectors/ja/GloVe/ipadic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = ipadic, jsar_class = 2, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/unidic, run_name = 0, word_embs_file = vectors/ja/GloVe/unidic/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = unidic, jsar_class = 2, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/jumanpp, run_name = 0, word_embs_file = vectors/ja/GloVe/jumanpp/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = jumanpp, jsar_class = 2, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/spm/8000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/8000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 8000, jsar_class = 2, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/spm/16000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/16000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 16000, jsar_class = 2, cuda = 0"
source my_path_config.sh; python main.py --config_file config/jSAR.conf --overrides "exp_name = exp/ja/SAR/spm/32000, run_name = 0, word_embs_file = vectors/ja/GloVe/spm/32000/300d.txt, do_pretrain = 1, do_target_task_training = 0, word_segmentation = spm, spm_vocabsize = 32000, jsar_class = 2, cuda = 0"
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
python scripts/calc_avg_length_all.py data/ja/RTE/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|10586|17.844133761571886|14.121409610935777|2|8.0|13.0|24.0|126
unidic|10586|20.8597203854147|15.633546398068882|3|10.0|15.0|28.0|138
spm-8000|10586|22.00443982618553|16.265093242959594|4|10.0|16.0|29.75|144
spm-16000|10586|19.193840921972416|14.000574326389003|3|9.0|14.0|25.0|124
spm-32000|10586|17.14670319289628|12.485121203202851|3|8.0|13.0|23.0|112
sudachi|10586|18.44247118836199|14.151662475393753|2|8.0|14.0|25.0|121
ipadic|10586|19.51369733610429|14.1302091521189|3|9.0|15.0|26.0|127


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
python scripts/calc_avg_length_all.py data/ja/WNLI/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|7424|11.203394396551724|4.222286583749785|4|8.0|10.0|14.0|29
unidic|7424|13.636449353448276|4.587625327215494|6|10.0|13.0|16.0|35
spm-8000|7424|14.625404094827585|5.022782803273753|6|11.0|14.0|18.0|43
spm-16000|7424|12.785425646551724|4.09503193035602|5|10.0|12.0|15.0|37
spm-32000|7424|11.322467672413794|3.5791920727101916|4|9.0|11.0|13.0|34
sudachi|7424|12.234240301724139|4.3459264287550505|5|9.0|11.0|15.0|34
ipadic|7424|13.13860452586207|4.259882904845714|6|10.0|12.0|16.0|35


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
python scripts/calc_avg_length_all.py data/ja/DP/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|114424|11.999632944137593|6.159068279974928|1|7.0|11.0|16.0|53
unidic|114424|14.222715514227785|6.713874119550589|2|9.0|13.0|18.0|62
spm-8000|114424|15.66875830245403|7.439031405870661|1|10.0|14.0|20.0|67
spm-16000|114424|13.60506537090121|6.491419551403433|1|9.0|13.0|17.0|57
spm-32000|114424|12.177515206600013|5.810076958120026|1|8.0|11.0|15.0|53
sudachi|114424|12.580018178004615|6.204950454065117|1|8.0|12.0|16.0|50
ipadic|114424|13.759106481157799|6.4151156738313455|2|9.0|13.0|17.0|57


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
python scripts/calc_avg_length_all.py data/ja/SAA/books/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|4000|139.85825|110.82537686350315|1|69.0|111.0|180.0|1783
unidic|4000|164.554|125.89941653558209|4|84.0|130.0|210.0|2163
spm-8000|4000|180.58575|138.68836521834663|4|93.0|144.0|228.0|2748
spm-16000|4000|156.57825|120.89711897699424|3|81.0|125.0|197.0|2433
spm-32000|4000|140.1215|108.3927291738242|3|72.0|111.0|177.0|2173
sudachi|4000|159.09525|120.73935223214302|3|80.0|126.0|203.0|1885
ipadic|4000|157.63725|118.7681719251311|4|80.0|125.5|201.0|1875

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
python scripts/calc_avg_length_all.py data/ja/SAA/dvd/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|4000|133.63825|110.33380437081603|1|61.0|103.0|176.0|1706
unidic|4000|159.53925|121.88970202374563|5|79.0|126.0|208.0|2196
spm-8000|4000|181.68|137.49596030429404|11|90.0|144.0|235.0|2317
spm-16000|4000|157.4715|119.89147045453234|10|78.0|124.0|203.0|2046
spm-32000|4000|140.94175|107.5998181082919|9|70.0|111.0|181.0|1810
sudachi|4000|153.628|116.95348697666094|4|75.0|121.0|201.0|2085
ipadic|4000|152.2935|115.8189097589422|5|75.0|120.0|197.25|2080

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
python scripts/calc_avg_length_all.py data/ja/SAA/music/
```

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|4000|113.44475|92.87286443002337|1|52.0|89.0|150.0|916
unidic|4000|138.93375|104.7191212765725|8|69.0|109.0|179.0|1042
spm-8000|4000|160.116|118.75162754253097|9|81.0|126.0|205.0|1114
spm-16000|4000|138.79375|103.02583030938163|9|70.0|109.0|179.0|1004
spm-32000|4000|123.859|91.7921054285171|7|63.0|98.0|159.0|896
sudachi|4000|131.85525|99.52674664349027|6|65.0|103.0|171.0|1015
ipadic|4000|130.52|98.19884215203355|8|65.0|102.0|168.25|995


## SAR (sentiment analysis rakuten)

`data/ja/SAR-2` and `data/ja/SAR-5`

```shell
==SAR-2==

# train.tsv: 1453723
 690081 0
 763642 1

# dev.tsv: 2000
    940 0
   1060 1
      
# test.tsv: 1420
    696 0
    713 1
    
==SAR-5==

# train.tsv: 1819704
 335368 1
 354872 2
 365591 3
 373941 4
 389932 5

# dev.tsv: 2000
    366 1
    415 2
    390 3
    368 4
    461 5
      
# test.tsv: 1473
    344 1
    352 2
     63 3
    315 4
    398 5

# Text length (# of tokens)
python scripts/calc_avg_length_all.py data/ja/SAR-2
```

__SAR-2__

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|1457132|41.19068416588202|11.742632808293994|5|32.0|40.0|49.0|104
unidic|1457132|48.55201656404499|13.193451026688848|12|38.0|47.0|58.0|108
spm-8000|1457132|56.64820277092261|15.001360109399181|21|45.0|54.0|67.0|121
spm-16000|1457132|49.055283941331325|13.195766454104424|18|39.0|47.0|58.0|113
spm-32000|1457132|44.20342700592671|11.962153882737852|15|35.0|43.0|53.0|103
sudachi|1457132|46.34754847192979|12.838195279879898|7|36.0|45.0|55.0|100
ipadic|1457132|46.7410481685942|12.756433223590845|12|37.0|45.0|56.0|99

__SAR-5__

Name|Text|Mean|Std|Min|25%|50%|75%|Max
-|-|-|-|-|-|-|-|-
jumanpp|1823176|41.06227923140717|11.702974748528234|5|32.0|39.0|49.0|106
unidic|1823176|48.38837446302496|13.144836993942738|9|38.0|46.0|58.0|108
spm-8000|1823176|56.39616800572188|14.96102535249125|21|44.0|54.0|67.0|121
spm-16000|1823176|48.826825824824375|13.15298633003055|18|38.0|47.0|58.0|113
spm-32000|1823176|43.99201174214667|11.92272028248654|15|35.0|42.0|52.0|103
sudachi|1823176|46.20736176869375|12.794897921529376|5|36.0|44.0|55.0|100
ipadic|1823176|46.57348769400212|12.708009041393513|9|36.0|45.0|55.0|99
