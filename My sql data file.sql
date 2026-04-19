CREATE DATABASE browser_ai;
USE browser_ai;

CREATE TABLE history_data (
    id BIGINT,
    url TEXT,
    title TEXT,
    visit_count INT,
    last_visit_time VARCHAR(50),
    visit_time VARCHAR(50),
    category VARCHAR(100)
);


SELECT * FROM history_data LIMIT 20;

/* Category count*/
SELECT category, COUNT(*) AS total
FROM history_data
GROUP BY category;

/*top visited titles*/
SELECT title, SUM(visit_count) AS visit_count
FROM history_data
GROUP BY title
ORDER BY visit_count DESC
LIMIT 10;

/* Most Recent Activity */
SELECT title, visit_time
FROM history_data
ORDER BY id DESC
LIMIT 10;

/* Category wise total usage*/
SELECT category, SUM(visit_count) AS total
FROM history_data
GROUP BY category
ORDER BY total DESC;
/* Top Productive titles */
SELECT title, visit_count
FROM history_data
WHERE category IN ('Learning','Career','Productivity')
ORDER BY visit_count DESC
LIMIT 10;
/* Top Distracting titles*/
SELECT title, visit_count
FROM history_data
WHERE category IN ('Entertainment','Social Media')
ORDER BY visit_count DESC
LIMIT 10;