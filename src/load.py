import boto3
from botocore.exceptions import BotoCoreError, ClientError
from io import BytesIO


def write_data_to_s3(df, bucket_name, s3_key):
    """Write a pandas DataFrame to S3 as a Parquet file."""

    s3_client = boto3.client("s3")

    try:
        # Create an in-memory buffer
        parquet_buffer = BytesIO()

        # Convert DataFrame to Parquet
        df.to_parquet(
            parquet_buffer,
            index=False,
            engine="pyarrow"
        )

        # Move buffer pointer back to the beginning
        parquet_buffer.seek(0)

        # Upload Parquet data to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=parquet_buffer.getvalue()
        )

        print(
            f"Successfully wrote DataFrame to "
            f"s3://{bucket_name}/{s3_key}"
        )

        return True

    except ClientError as e:
        print(f"S3 Client Error: {e}")
        return False

    except BotoCoreError as e:
        print(f"AWS BotoCore Error: {e}")
        return False