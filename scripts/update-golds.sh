#!/bin/bash -l

set -e

MYHOME=/data/ssd1/home/${USER}
MYEW=${MYHOME}/combustion
MYEWM=${MYEW}/exawind-manager
MYGOLDS=${MYEW}/golds/current
DATE=$(date -I)

cmd() {
  echo "+ $@"
  eval "$@"
}

copy() {
  SPEC=${1}
  GOLD_SPEC_DIR=${2}
  GOLD_DIR=${3}

  echo ""
  echo "Copying ${SPEC} golds..."
  SPEC_DIR=$(spack location -i ${SPEC})
  cmd "rm -r ${GOLD_DIR}/${GOLD_SPEC_DIR}/*"
  cmd "cp -R ${SPEC_DIR}/golds/Linux ${GOLD_DIR}/${GOLD_SPEC_DIR}/"
}

cmd "cd ${MYEWM}"
cmd "source shortcut.sh" || true
cmd "spack env activate ${DATE}"

for APP in pelec pelelmex
do
  GOLD_DIR=${MYGOLDS}/${APP}

  #~asan%llvm
  SPEC=${APP}~asan%llvm
  GOLD_SPEC_DIR=clang-cpu
  copy ${SPEC} ${GOLD_SPEC_DIR} ${GOLD_DIR}

  #+asan%llvm
  SPEC=${APP}+asan%llvm
  GOLD_SPEC_DIR=clang-cpu-asan
  copy ${SPEC} ${GOLD_SPEC_DIR} ${GOLD_DIR}

  #~cuda%gcc
  SPEC=${APP}~cuda%gcc
  GOLD_SPEC_DIR=gcc-cpu
  copy ${SPEC} ${GOLD_SPEC_DIR} ${GOLD_DIR}

  #+cuda%gcc
  SPEC=${APP}+cuda%gcc
  GOLD_SPEC_DIR=gcc-gpu
  copy ${SPEC} ${GOLD_SPEC_DIR} ${GOLD_DIR}
done
