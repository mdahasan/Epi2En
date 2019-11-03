# Epi2En

Epi2En is a Convolutional neural network based enhancer prediction tool. The tool uses epigenetic features to predict enhancer regions. The training and testing was performed in multiple human cell-lines. The enhancer data was collected from previously published work and the epigenetic features were collected from ENCODE project database.

## Data Preprocessing

### Converting `bigWig` file to `bed` file
The dataset provided contains ChIP-seq data collected from ENCODE. The directory contains seperate directory for each cell-line data. Each of those directory contains the `.bigWig` file and a tool `bigWigToBedGraph` to convert the `bigWig` file into `bed` file. A bash script is provided to run and convert all the `bigWig` files in a directory to convert into `bed` files. Comment/uncomment the bash file to run and convert `bigWig` files inside each directory.

```
./run_bigWig_to_bed.sh
```

After running this bash script each of the directory (cell-line) will contain the `bed` files for each of the epigenetics marks of each cell-line.

### Process `bed` files to make input for Epi2En