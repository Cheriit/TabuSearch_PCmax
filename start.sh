#!/bin/bash
for file in ./data/*; do python main.py $(echo $file | cut -d"/" -f3); done;
