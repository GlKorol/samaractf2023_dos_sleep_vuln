#!/bin/bash
for (( ; ; ))
do
python3 checker.py $1 && sleep $2
done