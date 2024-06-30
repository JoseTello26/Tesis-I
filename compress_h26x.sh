#!/bin/bash

# Verificar que se hayan proporcionado todos los parámetros necesarios
if [ "$#" -ne 7 ]; then
    echo "Uso: $0 <test> <dimensiones> <framerate> <bitrate> <preset> <threads> <calidad>"
    echo "Ejemplo: $0 1 1920x1080 120 1024k faster 8 5"
    exit 1
fi

# Asignar parámetros a variables
TEST=$1
VIDEO_DIMENSIONS=$2
FRAMERATE=$3
BITRATE=$4
PRESET=$5
THREADS=$6
QUALITY=$7

INPUT_FILE="test${TEST}/input.yuv"
echo $INPUT_FILE

OUTPUT_DIR="test${TEST}/${BITRATE}"
mkdir ${OUTPUT_DIR}

# Ejecutar ffmpeg con diferentes codecs
for CODEC in "libx264" "libx265" "libvvenc"; do
    if [ "$CODEC" == "libvvenc" ]; then
        OUTPUT_FILE="${OUTPUT_DIR}/output_${CODEC#lib}_${BITRATE}.266"
    else
        OUTPUT_FILE="${OUTPUT_DIR}/output_${CODEC#lib}_${BITRATE}.mp4"
    fi
    
    ffmpeg -f rawvideo -pix_fmt yuv420p -s:v $VIDEO_DIMENSIONS -r $FRAMERATE -i $INPUT_FILE \
           -c:v $CODEC -q $QUALITY -preset $PRESET -threads $THREADS -b:v $BITRATE $OUTPUT_FILE
done
