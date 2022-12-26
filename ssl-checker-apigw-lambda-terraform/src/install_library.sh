#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp -r venv/lib/python3.9/site-packages/* .
rm -rf venv
