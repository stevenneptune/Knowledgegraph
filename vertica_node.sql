SELECT COUNT(*)
FROM vertex
WHERE (
REGEXP_LIKE(NODE_LABEL,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(TYPE,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(FIRST_NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(LAST_NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(GENDER,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(EMAIL,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(SPEAKS,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(BROWSER_USED,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(LOCATION_IP,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(CONTENT,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(LANGUAGE,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(IMAGE_FILE,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(TITLE,'.*\bchina\b.*' ,'i') OR
REGEXP_LIKE(URL,'.*\bchina\b.*' ,'i') 
);