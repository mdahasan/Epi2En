"""
This code is the model for Deep learning model
"""

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping

from keras.layers.convolutional import Convolution1D, AveragePooling1D, MaxPooling1D
from keras.layers import Input
from keras.models import Model
from keras.layers.core import Dense, Dropout, Activation, Flatten

import scipy.stats as st
from sklearn.metrics import classification_report
from sklearn import metrics


# returns the TP, TN, FP and FN values
def getTPTNValues(test, testPred):
    TP, TN, FP, FN = 0, 0, 0, 0
    for i in range(len(testPred)):
        if test[i] == testPred[i] == 1:
            TP += 1
        if testPred[i] == 1 and test[i] != testPred[i]:
            FP += 1
        if test[i] == testPred[i] == 0:
            TN += 1
        if testPred[i] == 0 and test[i] != testPred[i]:
            FN += 1

    return TP, TN, FP, FN

def write_data_on_file(data, file_name):
    for i in range(len(data)):
        file_name.write(str(data[i]) + '\t')

    file_name.write('\n')


class NNModel(object):
    def __init__(self, data, name_of_exp):
        super(NNModel, self).__init__()

        self.data = data
        self.exp_name = name_of_exp

    def get_cross_validation_performance_of_epi(self):
        epi_dataset = self.data.get_epi_dataset()
        return run_cross_validation_with_only_epi_data(epi_dataset, self.exp_name)

    def get_cross_validation_performance_of_seq(self):
        seq_dataset = self.data.get_sequence_dataset()
        return run_cross_validation_with_only_seq_data(seq_dataset)


def run_cross_validation_with_only_epi_data(epi_dataset, exp_name):

    sample_matrices = epi_dataset['reshaped_sample_matrices']
    sample_label = epi_dataset['reshaped_sample_labels']
    # sample_regions = epi_dataset['sample_region']

    row, col = sample_matrices[0].shape
    num_classes = 2

    num_sample = len(sample_label)
    N1 = int(num_sample * 0.5)
    N2 = int(num_sample * 0.6)

    X_train = sample_matrices[0:N1]
    X_valid = sample_matrices[N1:N2]
    X_test = sample_matrices[N2:num_sample]

    all_data = sample_matrices[0:num_sample]

    # X_train = getScaledData(X_train)
    # X_valid = getScaledData(X_valid)
    # X_test = getScaledData(X_test)

    Y_train = sample_label[0:N1]
    Y_valid = sample_label[N1:N2]
    Y_test = sample_label[N2:num_sample]

    all_y = sample_label[0:num_sample]

    # convert class vectors to binary class matrices
    Y_train_one_hot = keras.utils.to_categorical(Y_train, num_classes)
    Y_valid_one_hot = keras.utils.to_categorical(Y_valid, num_classes)
    Y_test_one_hot = keras.utils.to_categorical(Y_test, num_classes)

    # train_regions = sample_regions[0:N1]
    # valid_regions = sample_regions[N1:N2]
    # test_regions = sample_regions[N2:num_sample]

    all_y_one_hot = keras.utils.to_categorical(all_y, num_classes)

    input_shape = (row, col)
    class_weight = {1: 0.65,
                    0: 0.35}        # adding class weights since the dataset is imbalanced

    model = Sequential()
    model.add(Conv1D(128, 3, activation='relu', input_shape=input_shape))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2, padding = 'same'))
    model.add(Dropout(0.25))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2, padding = 'same'))
    model.add(Dropout(0.25))
    model.add(Flatten())

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()

    check_pointer_file_name = exp_name
    model.compile(loss = 'binary_crossentropy', optimizer = keras.optimizers.SGD(), metrics=['accuracy'])
    check_pointer = ModelCheckpoint(filepath=str(check_pointer_file_name) + '.hdf5', verbose=1, monitor='val_loss', save_best_only=True)
    early_stopper = EarlyStopping(monitor='val_loss', patience=10, verbose=0)

    history = model.fit(X_train, Y_train_one_hot,
              batch_size = 32,
              class_weight=class_weight,
              epochs = 100,
              verbose = 1,
              shuffle = True,
              validation_data = (X_valid, Y_valid_one_hot),
              callbacks = [check_pointer, early_stopper],
              )

    # history = model.fit(all_data, all_y_one_hot,
    #           batch_size = 32,
    #           class_weight=class_weight,
    #           epochs = 100,
    #           verbose = 1,
    #           shuffle = True,
    #           validation_data = (X_valid, Y_valid_one_hot),
    #           callbacks = [check_pointer, early_stopper],
    #           )

    # model evaluation
    # test_loss, test_acc = model.evaluate(X_test, Y_test_one_hot, verbose=0)

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
        'history': history,
    }

    ########## These files are for plotting AUC and AUC-PR #########
    # f_fpr = open(str(exp_name) + '_fpr.txt', 'a')
    # f_tpr = open(str(exp_name) + '_tpr.txt', 'a')
    # f_precision = open(str(exp_name) + '_precision.txt', 'a')
    # f_recall = open(str(exp_name) + '_recall.txt', 'a')
    # f_validation = open(str(exp_name) + '_for_validation.txt', 'a')
    #
    # write_data_on_file(fpr_test, f_fpr)
    # f_fpr.close()
    #
    # write_data_on_file(tpr_test, f_tpr)
    # f_tpr.close()
    #
    # write_data_on_file(precision_test, f_precision)
    # f_precision.close()
    #
    # write_data_on_file(recall_test, f_recall)
    # f_recall.close()

    # for i in range(len(Y_pred_label_test)):
    #     f_validation.write(str(test_regions[i]) + '\t' + str(Y_pred_label_test[i]) + '\t' + str(Y_test[i]) + '\n')
    # f_validation.close()

    return evaluationInfo


def run_cross_validation_with_only_seq_data(seq_dataset):
    sample_matrices = seq_dataset['sample_matrices']
    sample_labels = seq_dataset['sample_labels']

    row, col = sample_matrices[0].shape
    num_classes = 2

    num_sample = len(sample_labels)
    N1 = int(num_sample * 0.8)
    N2 = int(num_sample * 0.9)

    X_train = sample_matrices[0:N1]
    X_valid = sample_matrices[N1:N2]
    X_test = sample_matrices[N2:num_sample]

    X_train = X_train.reshape(X_train.shape[0], col, row, 1)
    X_test = X_test.reshape(X_test.shape[0], col, row, 1)
    X_valid = X_valid.reshape(X_valid.shape[0], col, row, 1)
    input_shape = (col, row, 1)

    Y_train = sample_labels[0:N1]
    Y_valid = sample_labels[N1:N2]
    Y_test = sample_labels[N2:num_sample]

    # convert class vectors to binary class matrices
    Y_train_one_hot = keras.utils.to_categorical(Y_train, num_classes)
    Y_valid_one_hot = keras.utils.to_categorical(Y_valid, num_classes)
    Y_test_one_hot = keras.utils.to_categorical(Y_test, num_classes)

    # input_shape = (row, col)
    class_weight = {1: 0.6,
                    0: 0.4}        # adding class weights since the dataset is imbalanced

    model = Sequential()
    model.add(Conv2D(32, kernel_size = (3, 3),
                         activation = 'relu',
                         input_shape = input_shape))

    model.add(Conv2D(64, (3, 3), padding= "same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()

    model.compile(loss = 'binary_crossentropy', optimizer = keras.optimizers.SGD(), metrics=['accuracy'])
    check_pointer = ModelCheckpoint(filepath='model.hdf5', verbose=1, monitor='val_loss', save_best_only=True)
    early_stopper = EarlyStopping(monitor='val_loss', patience=10, verbose=0)

    model.fit(X_train, Y_train_one_hot,
              batch_size = 32,
              class_weight=class_weight,
              epochs = 100,
              verbose = 1,
              shuffle = True,
              validation_data = (X_valid, Y_valid_one_hot),
              callbacks = [check_pointer, early_stopper],
              )

    test_loss, test_acc = model.evaluate(X_test, Y_test_one_hot, verbose=0)
    print "Accuracy: ", test_acc

    Y_pred = model.predict(X_test)
    Y_pred_label = np.argmax(np.round(Y_pred), axis = 1)

    print Y_pred_label
    print "______________"
    print Y_test

    print(classification_report(Y_test, Y_pred_label, labels=[0, 1]))


    return test_acc, classification_report
