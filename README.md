# CSV Reader

## Description
This program receives a csv file as an input in order to extract the data and input it into a database.
This program is executable from the command line.

ex: ```./csv_reader.py <csv-file> ```

## Quick Startup
To run this program on your machine, _FORK_ and clone [this](https://github.com/jtruelas/csvReader.git) repo.
```
user ~ $ mkdir new_directory
user ~ $ git clone repo_url new_directory
user ~ $ cd new_directory
```
If you don't already have python go [here](https://www.python.org/downloads/) to download it. Make sure you check the box _Add python to PATH_ during the installation process.

Go to the download [site](https://www.sqlite.org/download.html) for sqlite3.

_*Make sure to click on the link that is designated as the bundle of command-line tools for your operating system._

Before unzipping the file, create a new directory to place sqlite. 
After unzipping the file go to your environment variables.

For windows: Start >> Control Panel >> System and Security >> System >> Advanced System Settings >> Environment Variables

From there look for System variable _Path_, click on it and click edit.
Click new and type in the path where sqlite was placed.

ex: ```C:\sqlite\```

Now you can accesss sqlite databases through the command line using:

```user ~ $ sqlite3```

Assuming you are in the directory where the clone was made, you should notice some sample csv files. In order to run the program enter in the following command:

```user <repo-directory> $ ./csv_reader.py <sample-csv-file>```

This command will give an output message summarizing the number of records inserted and the total number of records that exist in that specific table.

You can view the actual database created by this script (some.db) by:

_*Note: table names are the file names without the file extension_

```user {repo-directory} $ sqlite3```

```
sqlite> .open some.db
sqlite> select * from {table-name};
```

## Testing
To ensure the program is functioning as expected, you can either: 

**1. Run the program without an input:**

```./csv_reader.py```

This should cause the program to fail and produce an output message describing how to run the program correctly.

**2. Run the program with a non-csv file:**

```./csv_reader.py <some-file>.txt```

This should also cause the program to fail since the file does not have a .csv file extension.

**Running the program with a csv file should pass:**

```./csv_reader <some-file>.csv```