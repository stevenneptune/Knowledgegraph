SELECT *
FROM vertex
WHERE (
REGEXP_LILE(NODE_ID,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(NODE_LABEL,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(TYPE,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(FIRST_NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(LAST_NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(GENDER,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(EMAIL,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(SPEAKS,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(BROWSER_USED,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(LOCATION_IP,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(NAME,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(CONTENT,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(ID,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(LANGUAGE,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(IMAGE_FILE,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(TITLE,'.*\bchina\b.*' ,'i') OR
REGEXP_LILE(URL,'.*\bchina\b.*' ,'i') 
);