export BERT_BASE_DIR="./premodel/chinese_L-12_H-768_A-12"
export WEIBO_DIR="./result_data/"
 
python3 run_classifier.py \
  --task_name=emotion \
  --do_train=True \
  --do_eval=True \
  --data_dir=$WEIBO_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --train_batch_size=16 \
  --learning_rate=2e-5 \
  --num_train_epochs=4.0 \
  --max_seq_length=128 \
  --output_dir=./rest

