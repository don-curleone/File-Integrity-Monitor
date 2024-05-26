# File-Integrity-Monitor
## Overview
FIM(File Integrity Monitor) checks the integrity of the file by calculating its SHA256 hash and comparing it with a baseline hash. The baseline state is defined in a JSON file (baseline.json) that contains the absolute paths of the files and their corresponding hash values.

## Requirements
Linux OS\n
Python 3.7 or higher\n
Required Python packages: hashlib, json, smptblib, email, datetime

## Installation
''''
git clone https://github.com/don-curleone/File-Integrity-Monitor.git
cd File-Integrity-Monitor
''''

## Working

