-- 1. Select statement
SELECT Address, Title
FROM employees;

-- 2. Select all
SELECT * FROM employees;

-- 3. Select with limit display
SELECT Address, Title
FROM employees
LIMIT 5;

-- 4. Filter
select * from invoices
where Total between 1.98 and 4
limit 5;

select BillingState from invoices
where BillingState is null
limit 5;

select BillingCountry from invoices
-- here 'France' will not show
where BillingCountry = 'Germany' or 'France';

select BillingCountry from invoices
-- here 'France' will show
where BillingCountry in ('Germany', 'France');

select BillingCountry from invoices
where BillingCountry like '%ra%'
limit 5;