from src.extract import read_data_from_s3
from src.validate import validate_orders
from src.transform import transform_data
from src.load import write_data_to_s3


# AWS S3 configuration
BUCKET_NAME = "ecommerce-data-engineering-ghantasala-2026"

RAW_DATA_PATH = "raw/orders/orders.csv"
PROCESSED_DATA_PATH = "processed/orders/orders.parquet"


def main():
    print("\n================================")
    print("Starting ETL Pipeline")
    print("================================")

    # --------------------------------------------------
    # 1. EXTRACT
    # --------------------------------------------------
    print("\n[1/4] Extracting data from S3...")

    df = read_data_from_s3(
        BUCKET_NAME,
        RAW_DATA_PATH
    )

    if df is None:
        print("ETL Pipeline Failed: Data extraction failed.")
        return

    print(f"Extracted Records: {len(df)}")

    # --------------------------------------------------
    # 2. VALIDATE
    # --------------------------------------------------
    print("\n[2/4] Validating data...")

    validation_passed = validate_orders(df)

    if not validation_passed:
        print("ETL Pipeline Failed: Data validation failed.")
        return

    # --------------------------------------------------
    # 3. TRANSFORM
    # --------------------------------------------------
    print("\n[3/4] Transforming data...")

    transformed_df = transform_data(df)

    if transformed_df is None:
        print("ETL Pipeline Failed: Transformation failed.")
        return

    # --------------------------------------------------
    # 4. LOAD
    # --------------------------------------------------
    print("\n[4/4] Loading processed data to S3...")

    load_success = write_data_to_s3(
        transformed_df,
        BUCKET_NAME,
        PROCESSED_DATA_PATH
    )

    if not load_success:
        print("ETL Pipeline Failed: Data loading failed.")
        return

    print("\n================================")
    print("ETL Pipeline Completed Successfully")
    print("================================")


if __name__ == "__main__":
    main()