#!/bin/bash

db_set() {
  echo "$1,$2" >> storage.db
}

db_get() {
  grep "^$1," storage.db | sed -e "s/^$1,//" | tail -n 1
}


db_set 1 overwrite
db_get 1
