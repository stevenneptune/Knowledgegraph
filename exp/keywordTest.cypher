MATCH (m)
WHERE (any(prop in keys(m) WHERE toString(m[prop]) =~ {keyword}))
RETURN m as nod , ID(m) as ck

"keyword": "(?i).*\\b" + str.strip(keywords) + "\\b.*"
