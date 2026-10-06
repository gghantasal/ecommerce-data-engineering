
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import pandas as pd


def read_data_from_s3(bucket_name, s3_key):
    """Read a CSV file from an Amazon S3 bucket into a pandas DataFrame.

    :param bucket_name: S3 bucket name
    :param s3_key: Path/filename inside the S3 bucket
    :return: pandas DataFrame containing the CSV data
    """
    s3_client = boto3.client("s3")

    try:
        data = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        print(f"Successfully retrieved {s3_key} from s3://{bucket_name}/{s3_key}")
        df = pd.read_csv(data['Body'])  # Read the CSV content into a DataFrame
        return df

    except ClientError as e:
        print(f"S3 Client Error: {e}")
        return None
    except BotoCoreError as e:
        print(f"AWS BotoCore Error: {e}")
        return None