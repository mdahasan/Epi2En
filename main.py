"""
@author: Md Abid Hasan
contact: mhasa006@ucr.edu
University of California Riverside

Enhancer prediction from Epignetics and Sequence
"""

import os
import math
import argparse

from Process_and_make_dataset import *
from NN_model import *
from Load_model_run_test import *

parser = argparse.ArgumentParser(description="Ehancer prediction tool")

group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--crossvalidation', action='store_true', help='-c for Cross Validation')
group.add_argument('-a', '--acrosstest', action='store_true', help='-a for across cell line testing')
group.add_argument('-p', '--predictenhancers', action='store_true', help='-p predict enhancer regions')

parser.add_argument('-e', '--epidata', metavar='', required=True, help='-e for epigenetics dataset')
parser.add_argument('-r', '--region', metavar="", required=False, help='-s for corresponding epigenetics regions dataset')
parser.add_argument('-m', '--model', metavar="", required=False, help='-m for stored model to load')

parser.add_argument('-n', '--name', metavar="", required=True, help='-n for the name of the experiment')

args = parser.parse_args()


def pickle_data(D, file_name):
    filename = str(file_name)
    outfile = open(filename, 'wb')
    pickle.dump(D, outfile)
    outfile.close()


def main():
    name_of_the_experiment = args.name

    if args.crossvalidation:

        data = DataProcessing(args.epidata, args.region)
        model = NNModel(data, name_of_the_experiment)

        # cleaning file before each run
        if os.path.exists(name_of_the_experiment + '_tpr.txt'):
            os.remove(name_of_the_experiment + '_tpr.txt')
        if os.path.exists(name_of_the_experiment + '_fpr.txt'):
            os.remove(name_of_the_experiment + '_fpr.txt')
        if os.path.exists(name_of_the_experiment + '_precision.txt'):
            os.remove(name_of_the_experiment + '_precision.txt')
        if os.path.exists(name_of_the_experiment + '_recall.txt'):
            os.remove(name_of_the_experiment + '_recall.txt')
        if os.path.exists(name_of_the_experiment + '_for_validation.txt.txt'):
            os.remove(name_of_the_experiment + '_for_validation.txt.txt')

        fopen = open(str(name_of_the_experiment) + '_cross_validation_result.txt', 'w')
        fopen.write('Measure' + '\t' + 'Score' + '\t' + 'Data' + '\n')
        for iteration in range(1, 6):
            evaluation_info = model.get_cross_validation_performance_of_epi()
            roc_auc_train = evaluation_info['roc_auc_train']
            sen_train = evaluation_info['sensitivity_train']
            spe_train = evaluation_info['specificity_train']
            acc_train = evaluation_info['accuracy_train']
            precision_train = evaluation_info['precision_train']
            gm_train = math.sqrt(sen_train * spe_train)
            f1_train = evaluation_info['f1_train']

            roc_auc_test = evaluation_info['roc_auc_test']
            sen_test = evaluation_info['sensitivity_test']
            spe_test = evaluation_info['specificity_test']
            acc_test = evaluation_info['accuracy_test']
            precision_test = evaluation_info['precision_test']
            gm_test = math.sqrt(sen_test * spe_test)
            f1_test = evaluation_info['f1_test']

            # non_enh_perc = evaluation_info['non_enh_per']

            fopen.write('ROC_AUC' + '\t' + str(roc_auc_train) + '\t' + 'Training' + '\n' +
                        'Sensitivity' + '\t' + str(sen_train) + '\t' + 'Training' + '\n' +
                        'Specificity' + '\t' + str(spe_train) + '\t' + 'Training' + '\n' +
                        'GM' + '\t' + str(gm_train) + '\t' + 'Training' +'\n' +
                        'F1-Score' + '\t' + str(f1_train) + '\t' + 'Training' + '\n' +
                        'Accuracy' + '\t' + str(acc_train) + '\t' + 'Training' + '\n' +
                        'Precision' + '\t' + str(precision_train) + '\t' + 'Training' + '\n' +
                        # 'Non_Enh_Perc' + '\t' + str(non_enh_perc) + '\t' + 'Training' + '\n' +


                        'ROC_AUC' + '\t' + str(roc_auc_test) + '\t' + 'Test' + '\n' +
                        'Sensitivity' + '\t' + str(sen_test) + '\t' + 'Test' + '\n' +
                        'Specificity' + '\t' + str(spe_test) + '\t' + 'Test' + '\n' +
                        'GM' + '\t' + str(gm_test) + '\t' + 'Test' + '\n' +
                        'F1-Score' + '\t' + str(f1_test) + '\t' + 'Test' + '\n' +
                        'Accuracy' + '\t' + str(acc_test) + '\t' + 'Test' + '\n' +
                        'Precision' + '\t' + str(precision_test) + '\t' + 'Test' + '\n'
                        # 'Non_Enh_Perc' + '\t' + str(non_enh_perc) + '\t' + 'Test' + '\n'
                        )

        fopen.close()

        history = evaluation_info['history'].history
        training_acc = history['acc']
        training_loss = history['loss']
        valid_acc = history['val_acc']
        valid_loss = history['val_loss']

        f_learning = open(str(name_of_the_experiment) + '_learning.txt', 'w')
        for i in range(len(training_acc)):
            f_learning.write(str(float(training_acc[i])) + '\t' +
                             str(float(training_loss[i])) + '\t' +
                             str(float(valid_acc[i])) + '\t' +
                             str(float(valid_loss[i])) + '\n')

        f_learning.close()


    if args.acrosstest:
        data = DataProcessing(args.epidata, args.region)
        test_model = ModelLoad(data, args.model, name_of_the_experiment)

        fopen = open(str(name_of_the_experiment) + '_cross_validation.txt', 'w')

        for iteration in range(0, 5):
            print "Iteration: ", iteration + 1
            evaluation_info = test_model.get_across_cell_line_perfromance()
            roc_auc_train = evaluation_info['roc_auc_train']
            sen_train = evaluation_info['sensitivity_train']
            spe_train = evaluation_info['specificity_train']
            acc_train = evaluation_info['accuracy_train']
            precision_train = evaluation_info['precision_train']
            gm_train = math.sqrt(sen_train * spe_train)
            f1_train = evaluation_info['f1_train']

            roc_auc_test = evaluation_info['roc_auc_test']
            sen_test = evaluation_info['sensitivity_test']
            spe_test = evaluation_info['specificity_test']
            acc_test = evaluation_info['accuracy_test']
            precision_test = evaluation_info['precision_test']
            gm_test = math.sqrt(sen_test * spe_test)
            f1_test = evaluation_info['f1_test']

            fopen.write('ROC_AUC' + '\t' + str(roc_auc_train) + '\t' + 'Training' + '\n' +
                        'Sensitivity' + '\t' + str(sen_train) + '\t' + 'Training' + '\n' +
                        'Specificity' + '\t' + str(spe_train) + '\t' + 'Training' + '\n' +
                        'GM' + '\t' + str(gm_train) + '\t' + 'Training' +'\n' +
                        'F1-Score' + '\t' + str(f1_train) + '\t' + 'Training' + '\n' +
                        'Accuracy' + '\t' + str(acc_train) + '\t' + 'Training' + '\n' +
                        'Precision' + '\t' + str(precision_train) + '\t' + 'Training' + '\n' +
                        # 'Non_Enh_Perc' + '\t' + str(non_enh_perc) + '\t' + 'Training' + '\n' +


                        'ROC_AUC' + '\t' + str(roc_auc_test) + '\t' + 'Test' + '\n' +
                        'Sensitivity' + '\t' + str(sen_test) + '\t' + 'Test' + '\n' +
                        'Specificity' + '\t' + str(spe_test) + '\t' + 'Test' + '\n' +
                        'GM' + '\t' + str(gm_test) + '\t' + 'Test' + '\n' +
                        'F1-Score' + '\t' + str(f1_test) + '\t' + 'Test' + '\n' +
                        'Accuracy' + '\t' + str(acc_test) + '\t' + 'Test' + '\n' +
                        'Precision' + '\t' + str(precision_test) + '\t' + 'Test' + '\n'
                        # 'Non_Enh_Perc' + '\t' + str(non_enh_perc) + '\t' + 'Test' + '\n'
                        )

        fopen.close()

    if args.predictenhancers:
        data = DataProcessing(args.epidata, args.region)
        train_model = ModelLoad(data, args.model, name_of_the_experiment)

        train_model.get_enhancer_region_probability()


if __name__ == '__main__':
    main()
