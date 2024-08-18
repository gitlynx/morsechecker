#!/usr/bin/env bash

VENV_DIR="venv"
PYTHON_EXE=$(which python)
usage()
{
	echo ""
	echo "${0} <venv parameters> -- <application arguments>"
	echo ""
	exit 1
}

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Parse commandline options
VALID_ARGS=$(getopt -o abg:d: --long alpha,beta,gamma:,delta: -- "$@")
if [[ $? -ne 0 ]]; then
    exit 1;
fi

eval set -- "$VALID_ARGS"
while [ : ]; do
  case "$1" in
    -a | --alpha)
        echo "Processing 'alpha' option"
        shift
        ;;
    -b | --beta)
        echo "Processing 'beta' option"
        shift
        ;;
    -g | --gamma)
        echo "Processing 'gamma' option. Input argument is '$2'"
        shift 2
        ;;
    -d | --delta)
        echo "Processing 'delta' option. Input argument is '$2'"
        shift 2
        ;;
    --) shift; 
        break 
        ;;
  esac
done

# Does VENV directory exist?
if [ ! -d ${VENV_DIR} ] ; then
	${PYTHON_EXE} -m venv ${VENV_DIR}
fi

# Activate VENV
source ${VENV_DIR}/bin/activate

# Does MD5-sum file of requirements.txt match?
if [[ $(md5sum ${SCRIPT_DIR}/requirements.txt) != "$(cat ./${VENV_DIR}/requirements.md5)" ]]; then
	echo "updating libraries"
	${VENV_DIR}/bin/pip install -r ${SCRIPT_DIR}/requirements.txt
	md5sum ${SCRIPT_DIR}/requirements.txt > ${VENV_DIR}/requirements.md5
fi

# Run python with remaining arguments
${VENV_DIR}/bin/python $@


