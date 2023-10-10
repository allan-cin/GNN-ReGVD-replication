# Prepare the enviroment
- Install the requirements via
```shell
pip install -r req.txt
```


# 1. Prepare the data
- Download data from [MSR_20_Code_vulnerability_CSV_Dataset](https://github.com/ZeoVan/MSR_20_Code_vulnerability_CSV_Dataset)
- Use the cleaned CSV version: https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view
- Copy into `./dataset/msr`
- Run data splitter and formatter to get the split functions in jsonl format:
  - [data-splitter.py](dataset%2Fdata-splitter.py): split data into equal parts as json files
  - [preprocess-msr.py](dataset%2Fpreprocess-msr.py): convert json into jsonl

```shell
cd GNN-ReGVD-replication/dataset/
python data-splitter.py && python preprocess-msr.py
```

# 2. Run training
- The repo is provided with
  - [run.py](code%2Frun.py): originally by the author
  - [run-es.py](code%2Frun-es.py): added early stopping

```shell
cd GNN-ReGVD-replication/code/
python run-es.py --output_dir=./saved_models/reggnn_esLoss_dMSR_es_f1 \
  --model_type=roberta --tokenizer_name=microsoft/graphcodebert-base --model_name_or_path=microsoft/graphcodebert-base \
  --do_eval --do_test --do_train \
  --train_data_file=../dataset/msr/train_msr.jsonl --eval_data_file=../dataset/msr/valid_msr.jsonl --test_data_file=../dataset/msr/test_msr.jsonl \
  --train_batch_size 128 --eval_batch_size 128 --max_grad_norm 1.0 --evaluate_during_training \
  --gnn ReGGNN --learning_rate 5e-4 --epoch 100 --hidden_size 128 --num_GNN_layers 2 --format uni --window_size 5 \
  --seed 123456 2>&1 | tee -i ./saved_models/reggnn_esLoss_dMSR_es_f1/training_log.txt
```
