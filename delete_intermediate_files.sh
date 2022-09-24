#!/bin/bash

#Generate a empty folder at the first run
if [ ! -d BasicLEF ];then
	mkdir BasicLEF
fi

#clear Genus LEF BasicLEF LIB 
cd Genus
if [ -d LEF ];then
  rm -r LEF
fi

if [ -d BasicLEF ];then
  rm -r BasicLEF
fi

if [ -d LIB ];then
  rm -r LIB
fi
cd ..

#clear Innovus LEF BasicLEF LIBS 
cd Innovus
if [ -d LEF ];then
  rm -r LEF
fi

if [ -d BasicLEF ];then
  rm -r BasicLEF
fi

if [ -d LIBS ];then
  rm -r LIBS
fi
cd ..
