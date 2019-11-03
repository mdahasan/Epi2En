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

For example, if we want to process all the enhancer regions for Gm12878 cell-line, the `cell_line_directory_path` is the `path_to_Gm12878` that contains the processed epigenetics marker `bed` files of `Gm12878` and the `cell_line_region_file` is the file that contains `DEEP_GM12878_enhancers.txt` for DEEP data and `PEDLA_GM12878_enhancers.txt` for PEDLA data (one file at a time, either DEEP or PEDLA). Similar process for non-enhancer data. User can define the `type`. The `type` is used for the file extension that will be used later. We used `enh` for enhancer file processing and `nenh` for non-enhancer file processing. 

This code will produce same number of `.enh` and `.nenh` file as the `.bed` files representing each epigenetic markers.

The next step is to process these `.enh` and `.nenh` files to create the input for Epi2En. The script is provided in the `PreProcessing` directory here.

```
python Process_and_combine_epi_signals.py <cell_line_directory> <number_of_bins>
```

Here the `cell_line_directory` is similar as before i.e. `Gm12878` which now contains, along with the `bed` files, `enh` and `nenh` files. `number_of_bins` was selected as 10 (see manuscript). *Inside this script we have predefine the size of the non-enhancers regions we trained our model with. This may needs to be changed if the user desires.*

After running this script, it produces multiple `.pkl` file where each contains a fraction of the whole processed input. This was done for fast processing of `.pkl` files.

Finally, these seperate `.pkl` files are combined into one input file that contains all the enhancer/non-enahncer sample formatted into matrix format and added with label (1 for enhancers and 0 for non-enhancers)

```
python Build_epigenetics_dataset.py <cell_line_directory>
```

Similarly, here the `cell_line_directory` is any of the cell-line directory, i.e. `Gm12878`. For analysis we also produces a file that contains the regions of corresponding enhancer and non-enhancer samples.


## Training Epi2En

To train the model, the scripts are provided.

The `main.py` file contains multiple options for training the model

`-c` for cross-validation  
`-a` for across cell-line performance  
`-p` for enhancer region prediction on unknown regions  
  
`-e` to provide processed epigenetics data from the previous section. This is a `.pkl` file that contains the labelled matrix format sample data. (mandatory input)  
`-r` to provide processed enhancer/non-enhancer regions. This is a `.pkl` processed in the previous section (not a mandatory input)  
`-m` if an already trained model is available. This is used for the prediction of enhancers regions (not a mandatory input)  
  
`-n` the name of the experiment (mantadory input)  


For corss-validation

```
python main.py -c -e <processed_epigenetics_data> -n <name_of_the_experiment>
```

During training the model save the trained weights in `hdf5` format. We can use the `hdf5` weights later for the prediction.
  
For predicting using pre-trained model

```
python main.py -p -m <pre_trained_model> -n <name_of_the_experiment>
```

Here the `pre_trained_model` is the `hdf5` file generated during training. 

*The code will produce some additional results files which were used for the analysis purpose*
