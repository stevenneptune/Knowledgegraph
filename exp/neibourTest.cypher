MATCH (m)-[r]-(N)
WHERE toString (ID(M)) = {ck}
RETURN m as start, n as end ,r as relationships