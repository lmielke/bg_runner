# User Readme for Bg_runner python template package

Creates a empty **python package** using **pipenv** including all the relevant boilerpalte for a pyhon project with a single command.

Bg_runner itself serves as a **template** for your new package, so right after **bgr clone**, you can start using the new package.

When running **bgr clone** bg_runner is copied to your -t tgt_dir and re-structuring/re-naming is automatically done. 
NOTE: All code relevant for cloning and renaming the package is removed inside the target package. So the resulting target package cannot be used for cloning. Keep bg_runner if you want to create additional packages.

# Basic steps and commands
1. Clone bg_runner into your target directory
2. After activating bg_runner like 'pipenv shell' you can use the following command:
```shell
    cd .../bg_runner
    pipenv shell
    # minimal bgr clone
    bgr clone -pr 'my_superlib' -n 'my_superpackage' -a 'supi_alias' -t '/temp'
    # carefully choose your future project naming/install parameters
    # check if bg_runner environment is already active, and activeate if needed
    # the folowing command will create a new python package in /temp using a copy of bg_runner
    bgr clone -pr 'my_superlib' -n 'my_superpackage' -a 'supi_alias' -t '/temp' -p 3.13 --install
    # note that by omitting the --install flag, no python environment will be created
    # clone might ask you additional questions, i.e. missing parameters
    # You can now exit bgr and start coding your package
```
This will clone bg_runner into your new python package and install the environment using pipenv, so you can start coding right away.

When done, you can start coding your package in the newly created packag folder ('my_superpackage').
1. cd to your new package folder (i.e. '/temp/my_superlib')
2. Activate the environment using `pipenv shell`
3. To test the install sucess, run the following command:
```shell
    # retrieve some basic info about the package structure and its capabilities
    supi_alias info -i ['project', 'python'] or -v 1-3
```
Fields: 
- -i --infos Package infos [python, package] to be retreived, default: None
- -pr (project folder name),
- -n (package name), IMPORTANT NOTE: package name must be different from project folder name
- -t (target dir, where your project folder is created)
- -a (package alias) 
- -p python version [3.10, 3.11] to be used (will be set in your Pipfile)
- --install (bool) Triggers pipenv to install the environment using py_version.

<img src="https://drive.google.com/uc?id=1C8LBRduuHTgN8tWDqna_eH5lvqhTUQR4" alt="me_happy" class="plain" height="150px" width="220px">

## get and install
```shell
    git clone git@gitlab.com:larsmielke2/runner.git ./bg_runner
```
## Structure
### runner
- coding is in bg_runner/runner folder, add your .py modules there
- runner.apis contains the entry points to your package like info.py (usage: supi_alias entry_point)
- you can create as many entry points as needed 
- any entry_point.py module requires a main(*args, **kwargs) function as entry point
- __main__.py calls bg_runner/runner/apis/entry_point.py[provides as shell call args]


## USAGE
### 1. Clone runner into your target directory

### 2. Navigate to your new package and start coding
```shell 
    cd $tgt_dir
    pipenv shell
    supi_alias api_name [any args]
