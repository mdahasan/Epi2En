import numpy as np
import random
import keras
from keras.models import load_model

import scipy.stats as st
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.utils import shuffle


def reshape_matrix(matrix):
    row, col = matrix[0].shape
    reshaped_sample_index = 0
    reshaped_matrix = np.zeros((len(matrix), row, col), dtype = float)
    # this is to check if every sample has same lenght of histone marks signals
    for sample_id in range(len(matrix)):
        for i in range(row):
            for j in range(col):
                reshaped_matrix[reshaped_sample_index, i, j] = float(matrix[sample_id][i][j])
        reshaped_sample_index += 1

    return reshaped_matrix


def reshape_list(list):
    reshaped_list = np.zeros((len(list), 1), dtype = int)
    for sample_id in range(len(list)):
        reshaped_list[sample_id] = list[sample_id]

    return reshaped_list


class ModelLoad(object):
    def __init__(self, data, model, exp_name):
        super(ModelLoad, self).__init__()

        self.data = data
        self.model = model
        self.exp_name = exp_name

        self.epi_dataset = self.data.get_epi_dataset()

    def get_across_cell_line_perfromance(self):
        return run_across_cell_line_exp(self.epi_dataset, self.model, self.exp_name)

    def get_enhancer_region_probability(self):
        return run_enhancer_prob(self.epi_dataset, self.model, self.exp_name)

def write_data_on_file(data, file_name):
    for i in range(len(data)):
        file_name.write(str(data[i]) + '\t')

    file_name.write('\n')


def run_enhancer_prob(epi_data, model, exp_name):

    sample_matrices = epi_data['sample_matrices']
    sample_region = epi_data['sample_region']
    sample_matrices = reshape_matrix(sample_matrices)

    row, col = sample_matrices[0].shape
    num_classes = 2

    num_sample = len(sample_matrices)
    model = load_model(model)

    Y_pred = model.predict(sample_matrices)
    print Y_pred

    fopen = open('Predicted_K562_enhancer_regions_3.txt', 'w')

    for i in range(len(Y_pred)):
        chr = sample_region[i].split('_')[0]
        start = sample_region[i].split('_')[1]
        end = sample_region[i].split('_')[2]

        if Y_pred[i][0] > 0.5:
            label = "nenh"
        else:
            label = "enh"

        fopen.write(str(chr) + '\t' + str(start) + '\t' +
                    str(end) + '\t' + str(label) + '\n')

    fopen.close()

def run_across_cell_line_exp(epi_dataset, model, exp_name):

    sample_matrices = epi_dataset['sample_matrices']
    sample_label = epi_dataset['sample_labels']
    # sample_regions = epi_dataset['sample_region']

    # # shuffling new dataset
    c = list(zip(sample_matrices, sample_label))
    random.shuffle(c)
    sample_matrices, sample_label = zip(*c)

    # reshape for model compatibility
    sample_matrices = reshape_matrix(sample_matrices)
    sample_label = reshape_list(sample_label)

    row, col = sample_matrices[0].shape
    num_classes = 2

    num_sample = len(sample_label)
    N1 = int(num_sample * 0.1)
    N2 = int(num_sample * 0.2)

    X_train = sample_matrices[0:N1]
    X_valid = sample_matrices[N1:N2]
    X_test = sample_matrices[N2:num_sample]

    # X_train = getScaledData(X_train)
    # X_valid = getScaledData(X_valid)
    # X_test = getScaledData(X_test)

    Y_train = sample_label[0:N1]
    Y_valid = sample_label[N1:N2]
    Y_test = sample_label[N2:num_sample]

    # convert class vectors to binary class matrices
    Y_train_one_hot = keras.utils.to_categorical(Y_train, num_classes)
    Y_valid_one_hot = keras.utils.to_categorical(Y_valid, num_classes)
    Y_test_one_hot = keras.utils.to_categorical(Y_test, num_classes)

    # train_regions = sample_regions[0:N1]
    # valid_regions = sample_regions[N1:N2]
    # test_regions = sample_regions[N2:num_sample]

    model = load_model(model)

    # training performance evaluation
    Y_pred_train = model.predict(X_train)
    Y_pred_label_train = np.argmax(np.round(Y_pred_train), axis = 1)
    Y_pred_prob_train = model.predict_proba(X_train)
    Y_pred_prob_train = Y_pred_prob_train[:, 1]
    fpr_train, tpr_train, threshold_train = metrics.roc_curve(Y_train, Y_pred_prob_train)
    precision_train, recall_train, threshold_train = metrics.precision_recall_curve(Y_train, Y_pred_prob_train)

    roc_auc_train = metrics.roc_auc_score(Y_train, Y_pred_label_train)
    f1_score_train = metrics.f1_score(Y_train, Y_pred_label_train)

    # from confusion matrix
    conf = metrics.confusion_matrix(Y_train, Y_pred_label_train)
    TP_train = conf[0,0]
    FP_train = conf[0,1]
    FN_train = conf[1,0]
    TN_train = conf[1,1]

    sensitivity_train = float(TP_train) / float(TP_train + FN_train)
    specificity_train = float(TN_train) / float(TN_train + FP_train)
    accuracy_train = float(TP_train + TN_train) / float(TP_train + FP_train + FN_train + TN_train)
    prec_train = float(TP_train)/float(TP_train + FP_train)

    print(classification_report(Y_train, Y_pred_label_train, labels=[0, 1]))


    # testing performance evaluation
    Y_pred_test = model.predict(X_test)
    Y_pred_label_test = np.argmax(np.round(Y_pred_test), axis = 1)
    Y_pred_prob_test = model.predict_proba(X_test)
    Y_pred_prob_test = Y_pred_prob_test[:, 1]
    fpr_test, tpr_test, threshold_test = metrics.roc_curve(Y_test, Y_pred_prob_test)
    precision_test, recall_test, threshold_test = metrics.precision_recall_curve(Y_test, Y_pred_prob_test)

    roc_auc_test = metrics.roc_auc_score(Y_test, Y_pred_label_test)
    f1_score_test = metrics.f1_score(Y_test, Y_pred_label_test)

    # from confusion matrix
    conf = metrics.confusion_matrix(Y_test, Y_pred_label_test)
    TP_test = conf[0,0]
    FP_test = conf[0,1]
    FN_test = conf[1,0]
    TN_test = conf[1,1]

    sensitivity_test = float(TP_test) / float(TP_test + FN_test)
    specificity_test = float(TN_test) / float(TN_test + FP_test)
    accuracy_test = float(TP_test + TN_test) / float(TP_test + FP_test + FN_test + TN_test)
    prec_test = float(TP_test)/float(TP_test + FP_test)

    print(classification_report(Y_test, Y_pred_label_test, labels=[0, 1]))

    # dictionary to store evaluation stat
    evaluationInfo = {
        'roc_auc_train': roc_auc_train,
        'sensitivity_train': sensitivity_train,
        'specificity_train': specificity_train,
        'accuracy_train': accuracy_train,
        'precision_train': prec_train,
        'f1_train': f1_score_train,

        'roc_auc_test': roc_auc_test,
        'sensitivity_test': sensitivity_test,
        'specificity_test': specificity_test,
        'accuracy_test': accuracy_test,
        'precision_test': prec_test,
        'f1_test': f1_score_test,
    }

    print "ROC:", roc_auc_train, roc_auc_test
    print "Sensitivity: ", sensitivity_train, sensitivity_test
    print "Specificity: ", specificity_train, specificity_test
    print "Accuracy: ", accuracy_train, accuracy_test

    ########## These files are for plotting AUC and AUC-PR #########
    f_fpr = open(str(exp_name) + '_fpr.txt', 'a')
    f_tpr = open(str(exp_name) + '_tpr.txt', 'a')
    f_precision = open(str(exp_name) + '_precision.txt', 'a')
    f_recall = open(str(exp_name) + '_recall.txt', 'a')
    f_validation = open(str(exp_name) + '_for_validation.txt', 'a')

    write_data_on_file(fpr_test, f_fpr)
    f_fpr.close()

    write_data_on_file(tpr_test, f_tpr)
    f_tpr.close()

    write_data_on_file(precision_test, f_precision)
    f_precision.close()

    write_data_on_file(recall_test, f_recall)
    f_recall.close()

    # for i in range(len(Y_pred_label_test)):
    #     f_validation.write(str(test_regions[i]) + '\t' + str(Y_pred_label_test[i]) + '\t' + str(Y_test[i]) + '\n')
    # f_validation.close()

    return evaluationInfo


