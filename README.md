# File-Integrity-Monitor
## Overview
FIM(File Integrity Monitor) checks the integrity of the file by calculating its SHA256 hash and comparing it with a baseline hash. The baseline state is defined in a JSON file (baseline.json) that contains the absolute paths of the files and their corresponding hash values.

## Requirements
Linux OS<br/>
Python 3.7 or higher<br/>
Required Python packages: hashlib, json, smptblib, email, datetime

## Installation
````shell
git clone https://github.com/don-curleone/File-Integrity-Monitor.git
cd File-Integrity-Monitor
````

## baseline.json
Retrieve the absolute path of the file you intend to monitor. Compute its SHA256 hash and store it in <code>baseline.json</code>. The program iterates through the paths and  
compares the baseline hashes to the latest hashes.
<br/>
<i>Note: some paths may require root access.</i>\

## Configuration
Automate the process according to your preferences. Personally, I've set up the system to send emails every time the device starts up.
