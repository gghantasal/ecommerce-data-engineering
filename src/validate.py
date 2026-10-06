def validate_orders(df):
    """Validate order data and print a data quality report."""

    print("\nData Quality Report")
    print("-------------------")

    null_order_id = df["order_id"].isna().sum()
    null_customer_id = df["customer_id"].isna().sum()

    invalid_quantity = (df["quantity"] <= 0).sum()
    invalid_unit_price = (df["unit_price"] <= 0).sum()

    valid_statuses = ["Completed", "Pending", "Cancelled"]
    invalid_status = (~df["status"].isin(valid_statuses)).sum()

    print(f"Null order_id: {null_order_id}")
    print(f"Null customer_id: {null_customer_id}")
    print(f"Invalid quantity: {invalid_quantity}")
    print(f"Invalid unit_price: {invalid_unit_price}")
    print(f"Invalid status: {invalid_status}")

    # Determine whether validation passed
    if (
        null_order_id == 0
        and null_customer_id == 0
        and invalid_quantity == 0
        and invalid_unit_price == 0
        and invalid_status == 0
    ):
        print("\nValidation: PASSED")
        return True

    print("\nValidation: FAILED")
    return False