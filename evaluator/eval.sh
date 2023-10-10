python evaluator.py \
  --answers ../dataset/msr/test_msr.jsonl \
  --predictions ../code/saved_models/regcn_e100_dMSR_es_f1/predictions.txt

python evaluator.py \
  --answers ../dataset/msr/test_msr.jsonl \
  --predictions ../code/saved_models/regcn_e100_dMSR_es_loss/predictions.txt

#python evaluator.py \
#  --answers ../dataset/test.jsonl \
#  --predictions ../code/saved_models/regcn_e100/predictions.txt
