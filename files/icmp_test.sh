#!/bin/bash

numParam=$#

if [ $numParam -ne 2 ]
then
  echo "Error, there must be 2 parameters!"
  exit 1
else
  firstParam=$1
  if [ $firstParam == avg ]
  then
    retVal=`ping -c 10 -s 32760 $2 | grep rtt | awk '{print $4}' | cut -f2 -d/`
  elif [ $firstParam == loss ]
  then
    retVal=`ping -c 10 -s 32760 $2 | grep packets | awk '{print $6}' | sed 's/.$//'`
  fi
fi
echo $retVal

