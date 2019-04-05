#!/bin/bash

# DO NOT COMMIT CHANGES TO THIS FILE! Make a local copy and follow the
# instructions below.

# Copy this to /etc/profile.d/ to auto-set environment vars on login.
# Or, make a copy of this, customize, and run immediately before the training
# binary:
# cp path_config.sh ~/my_path_config.sh
# source ~/my_path_config.sh; python main.py --config ../config/demo.conf \
#   --overrides "do_pretrain = 0"

# Default environment variables for JSALT code. May be overwritten by user.
# See https://github.com/jsalt18-sentence-repl/jiant for more.

##
export JIANT_PROJECT_PREFIX=`pwd`
export JIANT_DATA_DIR=`pwd`/data
export WORD_EMBS_FILE=$HOME/data/embeddings/mono/en/GloVe/glove.840B.300d.txt
export FASTTEXT_MODEL_FILE=None
export FASTTEXT_EMBS_FILE=$HOME/data/embeddings/mono/en/fasttext/wiki-news-300d-1M.vec

export NFS_PROJECT_PREFIX=`pwd`
export NFS_DATA_DIR=`pwd`/data
