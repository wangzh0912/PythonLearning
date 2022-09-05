- [SELECT statement](#select-statement)
- [Creating tables](#creating-tables)

## SELECT statement
1. Select statement
    SELECT prod_name
        ,prod_id
        ,prod_price
    FROM Products;

2. Select all
   SELECT * FROM Products;

3. Limiting results: only want to see a sample
   SELECT AAPL
   FROM TimeSeriesData
   LIMIT 5;

## Creating tables

1. Example
    CREATE TABLE FundamentalData
    (
        Symbol      char(10)        PRIMARY KEY,
        ClosePrice  decimal(8, 2)   NOT NULL,
        MarketCap   decimal(8, 2)   NOT NULL,
        Desc        Varchar(750)    NULL
    );

2. Nulls and primary keys
    Primary keys should not be null values and must have a value. The null values is not an empty string.

3. Insert data to tables
   INSERT INTO FundamentalData
   (Symbol, ClosePrice, MarketCap, Desc);
   VALUES 
   ('AAPL', '403', '1000000', NULL);

4. Create temporary table which will be deleted when current session is terminated