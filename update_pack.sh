#!/bin/bash

cd iers/files
bash update.sh
cd -
fname="iers-$(date +%Y-%m-%d).tar.gz"
tar -zcvf $fname iers
echo "File ${fname} generated."
