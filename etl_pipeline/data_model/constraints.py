CONSTRAINTS = [
    """
    CREATE CONSTRAINT unique_org IF NOT EXISTS
    ON (c:Organization) ASSERT c.source_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT unique_url IF NOT EXISTS
    ON (u:Url) ASSERT u.url IS UNIQUE
    """,
    """
    CREATE CONSTRAINT unique_person IF NOT EXISTS 
    ON (c:Person) ASSERT c.source_id IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_events IF NOT EXISTS 
    ON (e:Event) ASSERT e.source_id IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_jobs IF NOT EXISTS 
    ON (j:Job) ASSERT j.matched_title IS UNIQUE 
    """,
    """
    CREATE CONSTRAINT unique_years IF NOT EXISTS 
    ON (y:Year) ASSERT y.year IS UNIQUE 
    """
    """
    CREATE CONSTRAINT unique_industry IF NOT EXISTS 
    ON (i:Industry) ASSERT i.industry IS UNIQUE 
    """
]