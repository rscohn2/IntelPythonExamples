# IntelPythonExamples

## Getting started

If you already have conda installed skip to 'Creating the example
environment'

Conda comes with Intel Python. You can get Intel Python at
https://software.intel.com/python-distribution. I recommend selecting
the local user install.

You can also get conda by installing Continuum Miniconda at
http://conda.pydata.org/miniconda.html

### Creating the example environment
    # upgrade to latest conda if you don't have 4.1.*
    # Give full path to conda if it is not on your path
    conda update conda

    # Tell conda you prefer the intel versions of packages in .condarc
    conda config --add channels intel

    # Create an environment with intel python and some other packages
    conda create -n nb -c rscohn2 intelpython3_examples python=3

    # After create completes, it will tell you how to activate the
    # environment.  You may have to give the full path to
    # the activate script. Alternatively, you can give the full path to python
    # and jupyter when trying the examples
    # the path is the installation path e.g ~/intel/intelpython35/envs/nb/bin/jupyter
### Launching the jupyter notebook
    jupyter notebook
