# BatchEmailScript

A simple python script for college event organisers.<br>
Generate and send certificates for mass number of participants through emails, based on a template image and csv file.

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
  
   Some libraries are pre-installed. If the following library are not installed, run the follwoing in CMD:

   ```bash
   pip install opencv-python
   ```

   ```bash
   pip install pandas
   ```

3. Replace the template.png and registrations.csv files in the directory and code.

4. Modify the following in the code.

## What to modify

1. Replace the file path/names everywhere in the code.

   ```python
   part_df = pd.read_csv('./registrations.csv')
   template = cv2.imread('template.png');
   filename = "template.png"
   ```

2. Choose your various font preferences from [open cv fonts](https://codeyarns.com/tech/2015-03-11-fonts-in-opencv.html#gsc.tab=0).

3. Modify the origin/starting pixels position in the certificate image (use MSpaint).

   ```python
   org = (563, 554)
   ```

4. Alter the column of values based on the csv file.

   ```python
   usn = part_df.iloc[index, 3]
   name = str(part_df.iloc[index, 2])
   to = part_df.iloc[index, 1]
   filename = "participants\\{}.png".format(part_df.iloc[index, 3])
   ```

4. Setup the App Password for gmail and replace in 'gmail_pass'.
   
   [How to generate SMTP app password in gmail](https://medium.com/rails-to-rescue/how-to-set-up-smtp-credentials-with-gmail-for-your-app-send-email-cf236d11087d)

5. Fill the remaining blanks accordingly in the code.

## Run the script.py file.
