## relationship.py
#%%

RELATIONSHIP_NAME_DIRECTION_MAP = {
    "HAS_URL": {"forward": "Has Url", "reverse": "Is Url of"},
    "PARENT_OF": {"forward": "", "reverse": ""},
    "ACQUIRED_BY": {"forward": "", "reverse": ""},
    "INVESTED_IN": {"forward": "", "reverse": ""},
    "LOCATED_IN": {"forward": "", "reverse": ""},
    "HAS_TITLE": {"forward": "", "reverse": ""},
    "FORMED_IN": {"forward": "", "reverse": ""},
    "EMPLOYER_OF": {"forward": "", "reverse": ""},
    "ATTENDED_BY": {"forward": "", "reverse": ""},
    "ATTENDED_SCHOOL": {"forward": "", "reverse": ""},
    "": {"forward": "", "reverse": ""},

}

RELATIONSHIPS = []

"""
HAS_URL
"""
temp = [
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "TWITTER"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "LINKEDIN"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "FACEBOOK"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "DOMAIN"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "TWITTER"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "LINKEDIN"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "DOMAIN"},
    {"source": "cb_investor_org", "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": "TWITTER"},
    {"source": "cb_investor_org", "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": "LINKEDIN"},
    {"source": "cb_investor_org", "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": "FACEBOOK"},
    {"source": "cb_investor_org", "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": "DOMAIN"},
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("HAS_URL",),
        "start_node_key": (("Organization",), {"property": "source_id", "field": x["start_node_field"]}),
        "end_node_key": (("Url",), {"property": "url", "field": x["end_node_field"]}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]

RELATIONSHIPS.extend(relationships)

temp = [
    {"source": "ss_person", "start_node_field": "ID", "end_node_field": "LINKEDIN"},
    {"source": "ss_person", "start_node_field": "ID", "end_node_field": "TWITTER"},
    {"source": "ss_person", "start_node_field": "ID", "end_node_field": "FACEBOOK"},
    {"source": "ss_person", "start_node_field": "ID", "end_node_field": "WEBSITE"},
    {"source": "cb_person", "start_node_field": "UUID", "end_node_field": "LINKEDIN"},
    {"source": "cb_person", "start_node_field": "UUID", "end_node_field": "TWITTER"},
    {"source": "cb_person", "start_node_field": "UUID", "end_node_field": "FACEBOOK"}
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("HAS_URL",),
        "start_node_key": (("Person",), {"property": "source_id", "field": x["start_node_field"]}),
        "end_node_key": (("Url",), {"property": "url", "field": x["end_node_field"]}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]

RELATIONSHIPS.extend(relationships)


"""
PARENT_OF
"""

temp = [
    {"source": "cb_parent", "start_node_field": "CB_PARENT_UUID", "end_node_field": "CB_UUID"},
    {"source": "ss_parent", "start_node_field": "ORGANIZATION_PARENT_ID", "end_node_field": "SS_ID"}
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("PARENT_OF",),
        "start_node_key": (("Organization",), {"property": "source_id", "field": x["start_node_field"]}),
        "end_node_key": (("Organization",), {"property": "source_id", "field": x["end_node_field"]}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]

RELATIONSHIPS.extend(relationships)

"""
ACQUIRED_BY
"""

relationship = {
    "source": "cb_acquisition",
    "properties_list": [
        {
            "property": "acquired_on",
            "field": "ACQUIRED_ON",
            "type": "datetime",
        },
        {
            "property": "acquisition_type",
            "field": "ACQUISITION_TYPE",
            "type": "string",
        },
        {
            "property": "disposition_of_acquired",
            "field": "DISPOSITION_OF_ACQUIRED",
            "type": "string",
        },
        {
            "property": "price",
            "field": "PRICE",
            "type": "float",
        },
        {
            "property": "price_currency_code",
            "field": "PRICE_CURRENCY_CODE",
            "type": "string",
        },
        {
            "property": "price_usd",
            "field": "PRICE_USD",
            "type": "float",
        },
        {
            "property": "status",
            "field": "STATUS",
            "type": "string",
        },
    ],
    "merge_key": ("ACQUIRED_BY",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ACQUIREE_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "ACQUIRER_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

"""
INVESTED_IN
"""

relationship = {
    "source": "cb_investor_investment",
    "properties_list": [],
    "merge_key": ("INVESTED_IN",),
    "start_node_key": (("Investor",), {"property": "source_id", "field": "CRUNCHBASE_INVESTOR_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "CRUNCHBASE_ORGANIZATION_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


"""
LOCATED_IN
"""
temp_loc = [
    {"source": "ss_org", "source_type": "Organization", "start_node_field": "SS_ID",
     "end_node_field": ["ORGANIZATION_CITY", "ORGANIZATION_STATE_CODE", "ORGANIZATION_COUNTRY_CODE"]},

    {"source": "cb_org", "source_type": "Organization", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID",
     "end_node_field": ["ORGANIZATION_CITY", "ORGANIZATION_STATE_CODE", "ORGANIZATION_COUNTRY_CODE"]},

    {"source": "ss_person", "source_type": "Person", "start_node_field": "ID",
     "end_node_field": ["CITY", "STATE_CODE", "COUNTRY_CODE"]},

    {"source": "cb_person", "source_type": "Person", "start_node_field": "UUID",
     "end_node_field": ["CITY", "STATE_CODE", "COUNTRY_CODE"]},

    {"source": "cb_investor_person", "source_type": "Person",
     "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": ["CITY", "REGION", "COUNTRY_CODE"]},

    {"source": "cb_investor_org", "source_type": "Organization",
     "start_node_field": "CRUNCHBASE_INVESTOR_UUID", "end_node_field": ["CITY", "REGION", "COUNTRY_CODE"]},
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("LOCATED_IN",),
        "start_node_key": ((x["source_type"],), {"property": "source_id", "field": x["start_node_field"]}),
        "end_node_key": (("Location",), {"property": label, "field": end_node_field}),
        "batch_size_factor": 1.0
    }
    for x in temp_loc
    for label, end_node_field in zip(["city", "state", "country"], x["end_node_field"])
]

RELATIONSHIPS.extend(relationships)

"""
FORMED_IN
"""

temp = [
    {"source": "ss_org", "start_node_field": "SS_ID"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID"}]

relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("FORMED_IN",),
        "start_node_key": (("Organization",), {"property": "source_id", "field": x["start_node_field"]}),
        "end_node_key": (("Year",), {"property": "year", "field": "YEAR_FOUNDED"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
RELATIONSHIPS.extend(relationships)


"""
ACQUIRED_IN
"""


relationships = [
    {
        "source": "cb_acquisition",
        "properties_list": [],
        "merge_key": ("ACQUIRED_IN",),
        "start_node_key": (("Organization",), {"property": "source_id", "field": "ACQUIREE_UUID"}),
        "end_node_key": (("Year",), {"property": "year", "field": "ACQUIRED_YEAR"}),
        "batch_size_factor": 1.0,
    }
]
RELATIONSHIPS.extend(relationships)


"""
HAS_TITLE
"""

temp = [
    {"source": "ss_person_to_org_current", "end_node_field": "PERSON_ID"},
    {"source": "cb_person_to_org_current", "end_node_field": "PERSON_UUID"},
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [
            {
                "property": "full_job_title",
                "field": "TITLE",
                "type": "string",
            }
        ],
        "merge_key": ("HAS_TITLE",),
        "start_node_key": (("Person",), {"property": "source_id", "field": x["end_node_field"]}),
        "end_node_key": (("Job",), {"property": "matched_title", "field": "MATCHED_TITLE"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
RELATIONSHIPS.extend(relationships)

"""
FORMER_TITLE
"""

temp = [
    {"source": "ss_person_to_org_former", "end_node_field": "PERSON_ID"},
    {"source": "cb_person_to_org_former", "end_node_field": "PERSON_UUID"}
]

relationships = [
    {
        "source": x["source"],
        "properties_list": [
            {
                "property": "full_job_title",
                "field": "TITLE",
                "type": "string",
            }
            
        ],
        "merge_key": ("FORMER_TITLE",),
        "start_node_key": (("Person",), {"property": "source_id", "field": x["end_node_field"]}),
        "end_node_key": (("Job",), {"property": "matched_title", "field": "MATCHED_TITLE"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
RELATIONSHIPS.extend(relationships)


"""
CURRENT_EMPLOYER_OF
"""

relationship = {
    "source": "ss_person_to_org_current",
    "properties_list": [
        {
            "property": "start_date",
            "field": "START_DATE",
            "type": "datetime"
        },
        {
            "property": "title",
            "field": "TITLE",
            "type": "string"
        },
        {
            "property": "role",
            "field": "ROLE",
            "type": "integer"
        },
    ],
    "merge_key": ("CURRENT_EMPLOYER_OF",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_ID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_ID"}),
    "batch_size_factor": 1.0,
}

RELATIONSHIPS.append(relationship)

relationship = {
    "source": "cb_person_to_org_current",
    "properties_list": [
        {
            "property": "start_date",
            "field": "START_DATE",
            "type": "datetime"
        },
        {
            "property": "title",
            "field": "TITLE",
            "type": "string"
        },
        {
            "property": "job_type",
            "field": "JOB_TYPE",
            "type": "string"
        },
    ],
    "merge_key": ("CURRENT_EMPLOYER_OF",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

"""
FORMER_EMPLOYER_OF
"""

relationship = {
    "source": "ss_person_to_org_former",
    "properties_list": [
        {
            "property": "start_date",
            "field": "START_DATE",
            "type": "datetime"
        },
        {
            "property": "end_date",
            "field": "END_DATE",
            "type": "datetime"
        },
        {
            "property": "title",
            "field": "TITLE",
            "type": "string"
        },
        {
            "property": "role",
            "field": "ROLE",
            "type": "integer"
        },
    ],
    "merge_key": ("FORMER_EMPLOYER_OF",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_ID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_ID"}),
    "batch_size_factor": 1.0,
}

RELATIONSHIPS.append(relationship)

relationship = {
    "source": "cb_person_to_org_former",
    "properties_list": [
        {
            "property": "start_date",
            "field": "START_DATE",
            "type": "datetime"
        },
        {
            "property": "end_date",
            "field": "END_DATE",
            "type": "datetime"
        },
        {
            "property": "title",
            "field": "TITLE",
            "type": "string"
        },
        {
            "property": "type",
            "field": "JOB_TYPE",
            "type": "string"
        },
    ],
    "merge_key": ("FORMER_EMPLOYER_OF",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

"""
ATTENDED_BY
"""

relationship = {
    "source": "cb_event_org",
    "properties_list": [
        {
            "property": "appearance_type",
            "field": "APPEARANCE_TYPE",
            "type": "string",
        }
    ],
    "merge_key": ("ATTENDED_BY",),
    "start_node_key": (("Event",), {"property": "source_id", "field": "EVENT_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "PARTICIPANT_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

relationship = {
    "source": "cb_event_person",
    "properties_list": [
        {
            "property": "appearance_type",
            "field": "APPEARANCE_TYPE",
            "type": "string"
        }
    ],
    "merge_key": ("ATTENDED_BY",),
    "start_node_key": (("Event",), {"property": "source_id", "field": "EVENT_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PARTICIPANT_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

"""
ATTENDED_SCHOOL
"""
relationship = {
    "source": "cb_person_degree",
    "properties_list": [
        {
            "property": "degree",
            "field": "DEGREE",
            "type": "string",
        },
        {
            "property": "subject",
            "field": "SUBJECT",
            "type": "string",
        },
        {
            "property": "start_date",
            "field": "START_DATE",
            "type": "datetime",
        },
        {
            "property": "end_date",
            "field": "END_DATE",
            "type": "datetime",
        }
    ],
    "merge_key": ("ATTENDED_SCHOOL",),
    "start_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "INSTITUTION_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)

"""
IN_INDUSTRY
"""
temp = [{"source" : "cb_org_industry", "start_field" : "CRUNCHBASE_ORGANIZATION_UUID"},
        {"source" : "ss_org_industry", "start_field" : "SS_ID"}]


relationships = [
    {
        "source": x["source"],
        "properties_list": [],
        "merge_key": ("IN_INDUSTRY",),
        "start_node_key": (("Organization",), {"property": "source_id", "field": x["start_field"]}),
        "end_node_key": (("Industry",), {"property": "industry", "field": "INDUSTRY"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
RELATIONSHIPS.append(relationships)
#%% md
## constraints.py
#%%
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