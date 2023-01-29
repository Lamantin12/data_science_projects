import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
def display_confusion_matrix(y_true, y_predicted) -> None:
    """Displays confusion matrix for binary classification

    Args:
        y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.
        y_predicted : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.
    """
    true_pos = y_true[y_true == y_predicted][y_true == 1].count()
    true_neg = y_true[y_true == y_predicted][y_true == 0].count()
    false_pos = y_true[y_true != y_predicted][y_true == 1].count()
    false_neg = y_true[y_true != y_predicted][y_true == 0].count()
    cm = np.array([[true_pos, false_pos],[false_neg, true_neg]])
    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    sns.heatmap(cm, 
                annot=True, 
                fmt='g',
                cbar=False, 
                xticklabels=['P', 'N'], 
                yticklabels=['P', 'N'],
                cmap='Blues',
                ax=ax[0]
               )
    sns.heatmap(cm / cm.sum(), 
                annot=True, 
                fmt='.2%',
                cbar=False, 
                xticklabels=['P', 'N'], 
                yticklabels=['P', 'N'],
                cmap='Blues',
                ax=ax[1]
               )
    fig.suptitle("Confusion matrices")
    ax[0].set_title("absolute values")
    ax[0].set_xlabel("predicted labels")
    ax[0].set_ylabel("actual labels")
    ax[1].set_title("percentages")
    ax[1].set_xlabel("predicted labels")
    ax[1].set_ylabel("actual labels")
    plt.show()

    print(f'accuracy = {accuracy_score(y_true, y_predicted)}')
    print(f'precision = {precision_score(y_true, y_predicted)}')
    print(f'recall = {recall_score(y_true, y_predicted)}')
    print(f'f1 = {f1_score(y_true, y_predicted)}')