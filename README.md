# Epi2En

Epi2En is a Convolutional neural network based enhancer prediction tool. The tool uses epigenetic features to predict enhancer regions. The training and testing was performed in multiple human cell-lines. The enhancer data was collected from previously published work and the epigenetic features were collected from ENCODE project database.

## Data Preprocessing

### Converting `bigWig` file to `bed` file
The dataset provided contains ChIP-seq data collected from ENCODE. The directory contains seperate directory for each cell-line data. Each of those directory contains the `.bigWig` file and a tool `bigWigToBedGraph` to convert the `bigWig` file into `bed` file. A bash script is provided to run and convert all the `bigWig` files in a directory to convert into `bed` files. Comment/uncomment the bash file to run and convert `bigWig` files inside each directory.

```
./run_bigWig_to_bed.sh
```

After running this bash script on each of the directory (cell-line) will contain the `bed` files for each of the epigenetics marks of each cell-line.

### Enahcer/Non-enhancer file
The dataset provided also contains the enhancer and non-enhancer regions used during the training of Epi2En. As mentioned these data was collected from two different sources, i.e. DEEP and PEDLA. The unzipped dataset contains two directory for DEEP and PEDLA data. Each of the directory contains the list of enhancer and non-enhancer regions for each cell-line provided by each source.


### Process `bed` files to make input for Epi2En

After all `bigWig` files are converted and stored as `bed` file in individual cell-line directory, we process each of the bed file based on the enhancer/non-enahancer regions provided in the cell-line specific enhancer/non-enhancer files in the unzipped dataset. The script for this stage is provided in the `PreProcessing` directory here.

```
python Store_enhancer_ChIP_seq_signals.py <cell_line_directory_path> <cell_line_region_file> <data_type>
```

For example, if we want to process all the enhancer regions for Gm12878 cell-line, the `cell_line_directory_path` is the `path_to_Gm12878` that contains the processed epigenetics marker `bed` files of `Gm12878` and the `cell_line_region_file` is the file that contains `DEEP_GM12878_enhancers.txt` for DEEP data and `PEDLA_GM12878_enhancers.txt` for PEDLA data. Similar process for non-enhancer data. User can define the `type`. The `type` is used for the file extension that will be used later. We used `enh` for enhancer file processing and `nenh` for non-enhancer file processing.