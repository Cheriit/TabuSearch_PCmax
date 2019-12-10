#!/bin/bash
for file in ./data/*; do echo $file; python main.py $(echo $file | cut -d"/" -f3); done;
