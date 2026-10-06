import pandas as pd


def transform_data(df):
    """Transform order data and return a cleaned DataFrame.

    :param df: pandas DataFrame containing raw order data
    :return: transformed pandas DataFrame, or None if required columns are missing
    """

    print("Input Records:", len(df))

    # Required columns
    required_columns = [
        "order_id",
        "customer_id",
        "order_date",
        "product",
        "category",
        "quantity",
        "unit_price",
        "country",
        "status"
    ]

    # Check required columns
    for col in required_columns:
        if col not in df.columns:
            print(f"Error: Column '{col}' is missing from the DataFrame.")
            return None

    # Remove duplicate orders
    df = df.drop_duplicates(subset=["order_id"]).copy()

    # Keep only valid quantity and unit price
    df = df[
        (df["quantity"] > 0) &
        (df["unit_price"] > 0)
    ].copy()

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # Keep only completed orders
    df = df[df["status"] == "Completed"].copy()

    # Calculate total order amount
    df["total_amount"] = (
        df["quantity"] * df["unit_price"]
    )

    print("Output Records:", len(df))

    return df