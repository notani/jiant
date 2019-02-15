#!/bin/bash

# Generic job script for all experiments on NYU CILVR machines.

#SBATCH --gres=gpu:1
#SBATCH --mem=30000
#SBATCH --constraint=gpu_12gb,pascal
# SBATCH --mail-type=ALL
# SBATCH --mail-user=yp913@nyu.edu
# Example usage:
# JIANT_OVERRIDES="exp_name = main-multi-task-glue, pretrain_tasks = glue, run_name = noelmo-do2-sd1, elmo_chars_only = 1, dropout = 0.2" JIANT_CONF="config/defaults.conf" sbatch ../nyu_cilvr_cluster.sbatch
# Log what we're running and where.
#!/bin/bash

export JIANT_PROJECT_PREFIX=edgeprobing
export JIANT_DATA_DIR=/misc/vlgscratch4/BowmanGroup/yp913/jiant/probing/data/probing_clean_dec2018/
export NFS_PROJECT_PREFIX=/nfs/jsalt/exp/nkim
export NFS_DATA_DIR=/=/misc/vlgscratch4/BowmanGroup/yp913/jiant/data/glue
export WORD_EMBS_FILE=/misc/vlgscratch4/BowmanGroup/yp913/jiant/data/glove.840B.300d.txt
export FASTTEXT_MODEL_FILE=None
export FASTTEXT_EMBS_FILE=None
module load anaconda3
source activate jiant_upgrade

python main.py --config_file config/edgeprobe_openai.conf
