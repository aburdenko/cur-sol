#! /bin/bash

gcloud beta ai custom-jobs local-run \
  --base-image=gcr.io/aburdenko-project/deepchem \
  --work-dir=./../train \
  --script=trainer.py \
  --output-image-uri=gcr.io/aburdenko-project/deepchem  
  #--gpu
  #--requirements=REQ
