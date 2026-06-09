INSERT INTO clean_transactions (
    step, type, amount, "nameOrig", "oldbalanceOrg", "newbalanceOrig",
    "nameDest", "oldbalanceDest", "newbalanceDest", "isFraud", "isFlaggedFraud",
    "isMissedFraud", "balanceDiscrepancy"
)
SELECT
    step,
    type,
    amount,
    "nameOrig",
    "oldbalanceOrg",
    "newbalanceOrig",
    "nameDest",
    "oldbalanceDest",
    "newbalanceDest",
    "isFraud",
    "isFlaggedFraud",
    ("isFraud" = 1 AND "isFlaggedFraud" = 0) AS "isMissedFraud",
    ("oldbalanceOrg" - amount - "newbalanceOrig") AS "balanceDiscrepancy"
FROM raw_transactions;