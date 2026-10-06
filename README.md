\# AWS E-commerce Data Engineering Pipeline



A Python-based ETL pipeline that extracts e-commerce order data from Amazon S3, validates data quality, transforms the dataset using Pandas, and loads the processed data back to Amazon S3 in Parquet format.



\## Architecture



```text

&#x20;                Amazon S3

&#x20;                   │

&#x20;                   │ Raw CSV

&#x20;                   ▼

&#x20;             ┌─────────────┐

&#x20;             │   Extract   │

&#x20;             │   Python    │

&#x20;             │   Boto3     │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;                    ▼

&#x20;             ┌─────────────┐

&#x20;             │  Validate   │

&#x20;             │   Pandas    │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;                    ▼

&#x20;             ┌─────────────┐

&#x20;             │ Transform   │

&#x20;             │   Pandas    │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;                    ▼

&#x20;             ┌─────────────┐

&#x20;             │    Load     │

&#x20;             │   Parquet   │

&#x20;             │   Boto3     │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;                    ▼

&#x20;                Amazon S3

&#x20;             Processed Data

```



\## Project Overview



This project demonstrates a simple cloud-based data engineering workflow using Python and AWS S3.



The pipeline:



1\. Reads raw order data from Amazon S3.

2\. Validates the incoming dataset.

3\. Removes duplicate orders.

4\. Filters invalid quantity and price values.

5\. Converts order dates to datetime.

6\. Keeps completed orders.

7\. Calculates total order amount.

8\. Writes the transformed dataset to Amazon S3 as Parquet.



\## Technologies



\* Python

\* Pandas

\* Boto3

\* Amazon S3

\* PyArrow

\* Parquet

\* Git

\* GitHub



\## S3 Data Structure



```text

s3://ecommerce-data-engineering-ghantasala-2026/



├── raw/

│   └── orders/

│       └── orders.csv

│

└── processed/

&#x20;   └── orders/

&#x20;       └── orders.parquet

```



\## ETL Workflow



\### 1. Extract



`src/extract.py`



Uses Boto3 to retrieve the raw CSV file from Amazon S3 and load it into a Pandas DataFrame.



```text

Amazon S3 → Boto3 → Pandas DataFrame

```



\### 2. Validate



`src/validate.py`



The pipeline performs basic data quality checks:



\* Null `order\_id`

\* Null `customer\_id`

\* Invalid quantity

\* Invalid unit price

\* Invalid order status



The pipeline stops if validation fails.



\### 3. Transform



`src/transform.py`



The transformation layer:



\* Removes duplicate orders

\* Removes invalid quantity and price records

\* Converts `order\_date` to datetime

\* Filters completed orders

\* Calculates `total\_amount`



```text

total\_amount = quantity × unit\_price

```



\### 4. Load



`src/load.py`



The transformed Pandas DataFrame is converted to Parquet in memory and uploaded to Amazon S3.



```text

Pandas DataFrame

&#x20;      ↓

&#x20;  PyArrow

&#x20;      ↓

&#x20;  Parquet

&#x20;      ↓

Amazon S3

```



\## Project Structure



```text

ecommerce-data-engineering/

│

├── data/

│   └── raw/

│       └── orders.csv

│

├── src/

│   ├── extract.py

│   ├── validate.py

│   ├── transform.py

│   └── load.py

│

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Requirements



\* Python 3.x

\* AWS account

\* Amazon S3 bucket

\* AWS CLI configured locally

\* IAM permissions to read and write to the required S3 bucket



\## Installation



Clone the repository:



```bash

git clone https://github.com/gghantasal/ecommerce-data-engineering.git

cd ecommerce-data-engineering

```



Create a virtual environment:



\### Windows



```powershell

python -m venv venvpython

```



Activate it:



```powershell

.\\venvpython\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



\## AWS Configuration



Configure AWS credentials using the AWS CLI:



```powershell

aws configure

```



The application uses Boto3 to obtain AWS credentials from the local AWS credential configuration.



\*\*Never commit AWS access keys, secret keys, or other credentials to GitHub.\*\*



\## Running the Pipeline



Run:



```powershell

python main.py

```



Example pipeline output:



```text

================================

Starting ETL Pipeline

================================



\[1/4] Extracting data from S3...

Extracted Records: 10



\[2/4] Validating data...



Data Quality Report

\-------------------

Null order\_id: 0

Null customer\_id: 0

Invalid quantity: 0

Invalid unit\_price: 0

Invalid status: 0



Validation: PASSED



\[3/4] Transforming data...

Input Records: 10

Output Records: 8



\[4/4] Loading processed data to S3...

Successfully wrote DataFrame to S3



================================

ETL Pipeline Completed Successfully

================================

```



\## Data Quality



The current implementation validates the following conditions before transformation:



| Check         | Description                      |

| ------------- | -------------------------------- |

| `order\_id`    | Must not be null                 |

| `customer\_id` | Must not be null                 |

| `quantity`    | Must be greater than zero        |

| `unit\_price`  | Must be greater than zero        |

| `status`      | Must be a supported order status |



Supported statuses:



```text

Completed

Pending

Cancelled

```



\## Future Enhancements



This project is intentionally being developed incrementally.



Planned improvements include:



\* PySpark processing

\* AWS Glue integration

\* Amazon Athena analytics

\* Apache Airflow orchestration

\* Incremental data processing

\* Data partitioning

\* CloudWatch monitoring and logging

\* Automated data quality framework

\* CI/CD using GitHub Actions

\* Infrastructure as Code

\* Unit and integration testing



\## Learning Objectives



This project demonstrates practical experience with:



\* Building Python ETL pipelines

\* Working with Amazon S3

\* Reading and writing cloud data

\* Data validation

\* Pandas transformations

\* Parquet data processing

\* AWS SDK integration using Boto3

\* Error handling

\* Git and GitHub version control

\* Designing modular ETL code



\## Author



\*\*Ghantasala Golla\*\*



Senior Software \& Data Engineer



Focus Areas:



\* Python

\* Data Engineering

\* PySpark

\* SQL

\* AWS

\* GCP

\* Azure

\* Apache Airflow

\* Data Platforms

\* GenAI / RAG



