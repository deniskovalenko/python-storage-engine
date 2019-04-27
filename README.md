# python-storage-engine
Simple key-value storage engine inspired by Designing Data Intensive Applications chapter on storage and retrieval

## Usage
`python3 write.py test-db key1 "first_value"`

`python3 write.py test-db key1 "overwrite"`

`python3 read.py test-db key1`

## ToDo:

* Write to new file once size threshold is reached
* Seach in all files
* Log merge background process