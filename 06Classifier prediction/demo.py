import xgboost as xgb
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
from sklearn.metrics import classification_report, precision_recall_fscore_support, accuracy_score, matthews_corrcoef, confusion_matrix

X = np.loadtxt('755/SampleFeature.csv', delimiter=',')
y = np.concatenate((np.ones(len(X)//2), np.zeros(len(X)//2)))

clf = xgb.XGBClassifier()
skf = StratifiedKFold(n_splits=5)
precision_list = []
recall_list = []
f1_score_list = []
acc_list = []
pr_aucs = []
mean_fpr = np.linspace(0, 1, 100)
fold_aucs = []
fold_auprs = []
for train_idx, test_idx in skf.split(X, y):
    X_train, y_train = X[train_idx], y[train_idx]
    X_test, y_test = X[test_idx], y[test_idx]
    clf.fit(X_train, y_train)
    y_pred_prob = clf.predict_proba(X_test)[:, 1]
    threshold = 0.5
    y_pred = np.where(y_pred_prob > threshold, 1, 0)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    np.save(f"Y_pre{len(precision_list)}.npy", y_pred_prob)
    np.save(f"Y_test{len(precision_list)}.npy", y_test)
    fold_aucs.append(roc_auc)
    fold_auprs.append(aupr)
    precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
    accuracy = accuracy_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_score_list.append(f1_score)
    acc_list.append(accuracy)
    mcc_list.append(mcc)
    spec_list.append(specificity)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"SPEC: {specificity:.4f}")
    print(f"F1-score: {f1_score:.4f}")
    print(f"MCC: {mcc:.4f}")
    with open("5-fold data.txt", "a") as f:
        f.write(f"\t\t{accuracy:.4f}\t  {precision:.4f}\t  {recall:.4f}\t  {specificity:.4f}\t  {f1_score:.4f}\t  {mcc:.4f}\n")
