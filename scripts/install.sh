#! /usr/bin/env bash
apt-get install vim
#wget -qO- https://raw.githubusercontent.com/docker/docker-install/master/install.sh | bash
apt-get -qq install docker.io
touch /var/run/docker.sock
chmod 666 /var/run/docker.sock
useradd -md /opt/docker docker
apt-get -qq install iproute2 uidmap
sudo -Hu docker SKIP_IPTABLES=1 bash < <(curl -fsSL https://get.docker.com/rootless)

#service docker start
