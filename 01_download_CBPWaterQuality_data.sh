#!/bin/bash

# If you get a permission error you may need to run
# chmod u+x 01_download_CBPWaterQuality_data.sh
# This adds executable permissions for your user to this script


OUTPUT_PATH="./WaterQuality_ChesapeakeBayProgram.csv"

echo $OUTPUT_PATH

if [ "$1" ]; then
    echo $1
    OUTPUT_PATH=$1
    # If the input argument is just a directory append the default filename
#     if [ -d "$1" ] ; then
# 	OUTPUT_PATH="{$1}{OUTPUT_PATH}"
#     else  # Otherwise pass full argument along as the output path
#         OUTPUT_PATH=$1
#     fi

    echo $OUTPUT_PATH

    # Create the given input directory, if it doesn't already exist
    OUTPUT_DIR="$(dirname "${OUTPUT_PATH}")"
    echo $OUTPUT_DIR
    mkdir -p $OUTPUT_DIR

elif [[ -d ./data/raw ]]; then
    echo Found `./data/raw/` folder
    OUTPUT_PATH="./data/raw/${OUTPUT_PATH}"
    echo $OUTPUT_PATH

else
    echo Downloading to current directory
fi

echo Downloading to $OUTPUT_PATH
curl https://data.chesapeakebay.net/api.CSV/WaterQuality/WaterQuality/12-31-2002/12-31-2022/0,1/2,4,6/12,13,15,35,36,2,3,7,33,34,23,24/HUC8/2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60/123 -o $OUTPUT_PATH

# one day version of the URL for testing
# curl 
# https://data.chesapeakebay.net/api.CSV/WaterQuality/WaterQuality/01-1-2022/01-02-2022/0,1/2,4,6/12,13,15,35,36,2,3,7,33,34,23,24/HUC8/2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60/123 
# -o $OUTPUT_PATH
