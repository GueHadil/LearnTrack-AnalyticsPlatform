-- Create keyspace
CREATE KEYSPACE IF NOT EXISTS learntrack
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

-- Use keyspace
USE learntrack;

-- Create table
CREATE TABLE IF NOT EXISTS course_engagement (
  courseid text,
  date date,
  count bigint,
  PRIMARY KEY (courseid, date)
);

-- Verify data
SELECT * FROM course_engagement;
