CREATE TABLE IF NOT EXISTS raw_transactions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    step INT NOT NULL,
    type VARCHAR(10) NOT NULL,
    amount NUMERIC(18,2) NOT NULL,
    "nameOrig" VARCHAR(20) NOT NULL,
    "oldbalanceOrg" NUMERIC(18,2) NOT NULL,
    "newbalanceOrig" NUMERIC(18,2) NOT NULL,
    "nameDest" VARCHAR(20) NOT NULL,
    "oldbalanceDest" NUMERIC(18,2) NOT NULL,
    "newbalanceDest" NUMERIC(18,2) NOT NULL,
    "isFraud" INT NOT NULL,
    "isFlaggedFraud" INT NOT NULL
);