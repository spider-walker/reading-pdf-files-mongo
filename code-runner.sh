#!/bin/sh

py readpdf.py > data/data2017.txt
py clean-up-pdf.py > data/output.txt
py prep-data-to-json.py > data/prep-data-to-json.json
py insert-into-mongo.py