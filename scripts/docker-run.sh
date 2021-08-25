#!/usr/bin/env bash
set -e
export DOCKER_SOCK=/opt/docker/.docker/run/docker.sock
export DOCKER_HOST=unix://$DOCKER_SOCK
export PATH=/opt/docker/bin:$PATH
export XDG_RUNTIME_DIR=/opt/docker/.docker/run
/opt/docker/bin/dockerd-rootless.sh --experimental --iptables=false --storage-driver vfs &
for i in $(seq 5); do [ ! -S "$DOCKER_SOCK" ] && sleep 2 || break; done
docker run $@
jobs -p
kill $(jobs -p)
