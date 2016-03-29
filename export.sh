#!/bin/bash


git archive master --prefix=PacketLossMon-$1/ | gzip > ../PacketLossMon-$1.tar.gz
