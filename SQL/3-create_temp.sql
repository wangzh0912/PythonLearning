
CREATE TEMPORARY TABLE calgary AS
(
	SELECT * FROM employees
    WHERE City = 'Calgary';
);

SELECT * FROM calgary;