#!/bin/bash

cd iers/files
bash update.sh
cd -
date_s=`date +%Y-%m-%d` 
tar -zcvf "iers-${date_s}.tar.gz" iers