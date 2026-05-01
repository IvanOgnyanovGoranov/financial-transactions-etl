CREATE TABLE IF NOT EXISTS raw_transactions (
    id SERIAL PRIMARY KEY,
    step INT NOT NULL,
    type VARCHAR(10) NOT NULL,
    amount NUMERIC(18,2) NOT NULL,
    nameOrig VARCHAR(20) NOT NULL,
    oldbalanceOrig NUMERIC(18,2) NOT NULL,
    newbalanceOrig NUMERIC(18,2) NOT NULL,
    nameDest VARCHAR(20) NOT NULL,
    oldbalanceDest NUMERIC(18,2) NOT NULL,
    newbalanceDest NUMERIC(18,2) NOT NULL,
    isFraud INT NOT NULL,
    isFraudFlagged INT NOT NULL
)