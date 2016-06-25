import os
os.system("conda metapackage --build-number 1 --build-string intel --depend intelpython3_core notebook ipykernel dask --license MIT --summary 'environment for intel python examples' intelpython3_examples 1")
os.system("anaconda upload /home/rscohn1/intel/intelpython35/conda-bld/linux-64/intelpython3_examples-1-intel.tar.bz2")
