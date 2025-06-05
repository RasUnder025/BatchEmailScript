# BatchEmailScript

A simple python script for college event organisers.<br>
Generate and send certificates for mass number of participants through emails.

> *Warning: Do not misuse this script for malicious intentions.*

## Pre-requisites

Python version: 3.10.15+<br>
Any python IDE (preferrably [Jupyter Notebook](https://jupyter.org/install) )

## Directory structure

```
.
├── participants
│   ├── usn1.png
│   ├── usn2.png
│   └── usn3.png
├── template.png
├── registrations.csv
├── script.py
└── README.md
```

## Setup

1. Clone the repository using CLI or UI

   ```bash
   gh repo clone RasUnder025/BatchEmailScript
   ```

2. Install the libraries
  
   Some libraries are pre-installed. If the following library are not installed, you may do so by:

   ```bash
   pip install opencv-python
   ```

   ```bash
   pip install pandas
   ```

3. Replace the template.png and registrations.csv files in the directory and code.

4. Setup the App Password for gmail and modify in the code.
   
   [How to generate SMTP app password in gmail](https://medium.com/rails-to-rescue/how-to-set-up-smtp-credentials-with-gmail-for-your-app-send-email-cf236d11087d)

5. Modify other blanks accordingly in the code.

## Run the script.py file.
