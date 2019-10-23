export BERT_BASE_DIR="./premodel/chinese_L-12_H-768_A-12"
export WEIBO_DIR="./result_data/"
export TRAINED_CLASSIFIER="./rest" 


python3 run_classifier.py \
  --task_name=emotion \
  --do_predict=true \
  --data_dir=$GLUE_DIR/MRPC \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=128 \
  --output_dir=./mrpc_output/
