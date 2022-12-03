#!/usr/bin/env bash

SCRIPT_DIR=$(
    cd "$(dirname "$0")" || exit
    pwd | xargs dirname
)

declare -a brew_packges=(
    'elastic/tap/elasticsearch-full'
    'elastic/tap/kibana-full'
)

if ! type -a brew >/dev/null 2>&1; then
    echo 'please install brew.'
    exit 1
fi

if ! brew tap elastic/tap >/dev/null; then
    brew tap elastic/tap
fi

brew install "${brew_packges[@]}"

ES_PATH_CONF="$SCRIPT_DIR/configs"
echo "elasticsearch config path is $ES_PATH_CONF"
KBN_PATH_CONF="$SCRIPT_DIR/configs"
echo "kibana config path is $ES_PATH_CONF"

brew services start 'elasticsearch-full'
brew services start 'kibana-full'
