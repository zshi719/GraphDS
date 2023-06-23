#%%
CONSTRAINTS = [
    """
    CREATE CONSTRAINT unique_org IF NOT EXISTS 
    FOR (o:Organization) REQUIRE o.source_id IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_url IF NOT EXISTS 
    FOR (u:Url) REQUIRE u.url IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_events IF NOT EXISTS 
    FOR (e:Event) REQUIRE e.source_id IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_person IF NOT EXISTS 
    FOR (c:Person) REQUIRE c.source_id IS UNIQUE 
    """
]