#! /bin/bash
#
#
# Install dependencies...
#
sudo apt-get install autoconf automake avahi-daemon build-essential git libasound2-dev libavahi-client-dev libconfig-dev libdaemon-dev libpopt-dev libssl-dev libtool xmltoman
sudo apt-get install libpulse-dev xxd libplist-dev libsodium-dev libgcrypt-dev libavutil-dev libavcodec-dev libavformat-dev
#
# Download source...
#
git clone https://github.com/mikebrady/nqptp.git
git clone https://github.com/mikebrady/shairport-sync.git
#
# Build and install...
#
# First nqptp..
#
cd nqptp/
autoreconf -fi
./configure --with-systemd-startup
make
sudo make install
sudo systemctl enable nqptp
sudo systemctl start nqptp
#
# Next shairport-sync
#
cd shairport-sync/
autoreconf -fi
./configure --with-avahi --with-ssl=openssl --with-systemd --with-pa --with-airplay-2
make clean
make
sudo make install
