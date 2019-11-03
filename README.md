# Epi2En

Epi2En is a Convolutional neural network based enhancer prediction tool. The tool uses epigenetic features to predict enhancer regions. The training and testing was performed in multiple human cell-lines. The enhancer data was collected from previously published work and the epigenetic features were collected from ENCODE project database.

## Data Preprocessing

The dataset provided contains ChIP-seq data collected from ENCODE. The directory contains seperate directory for each cell-line data. Each of those directory contains the `.bigWig` file and a tool `bigWigToBedGraph` to convert the `bigWig` file into `bed` file