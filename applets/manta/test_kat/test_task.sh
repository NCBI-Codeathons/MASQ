#!/usr/bin/env bash


TEST_NAME="test_task"

# dxWDL jar as an argument
DXWDL_JAR=$1

dx mkdir -p /Jun/test/tasks/${TEST_NAME}/


java -jar ${DXWDL_JAR} \
    compile ${TEST_NAME}.wdl -project project-FfG3k9Q97yFygXqZ4B39B2BV \
    -inputs ${TEST_NAME}.input.json \
    -destination /test/tasks/${TEST_NAME}/ \
    --imports ../ -f  | xargs dx run -f  ${TEST_NAME}.input.dx.json
