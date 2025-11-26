select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name FROM bears ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;
"""

select_all_bears_names_and_ages_ordered_by_age = """
SELECT name, age
FROM bears
ORDER BY age;
"""

select_all_bears_names_and_ages_ordered_by_age_desc = """
SELECT name, age
FROM bears
ORDER BY age DESC;
"""

select_youngest_bear = """
SELECT *
FROM bears
ORDER BY age ASC
LIMIT 1;
"""

select_oldest_bear = """
SELECT *
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

select_most_aggressive_bear = """
SELECT *
FROM bears
WHERE temperament='aggressive'
LIMIT 1;
"""

select_all_bears_alive = """
SELECT *
FROM bears
WHERE alive = 1;
"""

select_bears_with_name_sorted_alphabetically = """
SELECT *
FROM bears
WHERE name IS NOT NULL
ORDER BY name ASC;
"""
