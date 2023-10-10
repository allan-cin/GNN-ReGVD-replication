# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.
import sys
import numpy as np
from sklearn import metrics
import json

def read_answers(filename):
    answers = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            js = json.loads(line)
            answers[js['idx']] = js['target']
    return answers


def read_predictions(filename):
    predictions = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            idx, label = line.split()
            predictions[int(idx)] = int(label)
    return predictions


def calculate_scores(answers, predictions):
    acc = []
    answer_exist = []
    predictions_exist = []
    missing_count = 0
    for key in answers:
        if key not in predictions:
            missing_count += 1
            print(f"Missing prediction for index {key}")
            # sys.exit()
        else:
            answer_exist.append(answers[key])
            predictions_exist.append(predictions[key])
            acc.append(answers[key] == predictions[key])

    print(f"=== Missing predictions for {missing_count} records.")
    # {idx: class,...}
    # answer_exist = list(answers.values())
    # predictions_exist = list(predictions.values())

    tn, fp, fn, tp = metrics.confusion_matrix(answer_exist, predictions_exist).ravel()

    scores = {
        "Confusion matrix": f"TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}",
        # "Accuracy": np.mean(acc),
        "Accuracy": metrics.accuracy_score(answer_exist, predictions_exist),
        "Precision": metrics.precision_score(answer_exist, predictions_exist),
        "Recall": metrics.recall_score(answer_exist, predictions_exist),
        "F-measure": metrics.f1_score(answer_exist, predictions_exist),
        # "Precision Weighted": metrics.precision_score(answer_exist, predictions_exist, average='weighted',labels=np.unique(predictions_exist)),
        # "Recall Weighted": metrics.recall_score(answer_exist, predictions_exist, average='weighted',labels=np.unique(predictions_exist)),
        # "F-measure Weighted": metrics.f1_score(answer_exist, predictions_exist, average='weighted',labels=np.unique(predictions_exist)),
        "Precision-Recall AUC": metrics.average_precision_score(answer_exist, predictions_exist),
        "AUC": metrics.roc_auc_score(answer_exist, predictions_exist),
        "MCC": metrics.matthews_corrcoef(answer_exist, predictions_exist),
    }

    return scores


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Evaluate leaderboard predictions for Defect Detection dataset.')
    parser.add_argument('--answers', '-a', help="filename of the labels, in txt format.")
    parser.add_argument('--predictions', '-p', help="filename of the leaderboard predictions, in txt format.")

    args = parser.parse_args()
    answers = read_answers(args.answers)
    predictions = read_predictions(args.predictions)
    scores = calculate_scores(answers, predictions)
    print(json.dumps(scores, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
