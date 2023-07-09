NODES = []

"""
Organization nodes
"""

node = {
    "source": "ss_org",
    "labels": ("Organization", "Sourcescrub"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "SS_ID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "ORGANIZATION_NAME",
            "type": "string",
        },
        {
            "property": "phone_number",
            "field": "ORGANIZATION_PHONE",
            "type": "string",
        }
    ],
    "merge_key": (("Organization",), {"property": "source_id", "field": "SS_ID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

node = {
    "source": "cb_org",
    "labels": ("Organization", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "CRUNCHBASE_ORGANIZATION_UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "ORGANIZATION_NAME",
            "type": "string",
        },
        {
            "property": "company_type",
            "field": "COMPANY_TYPE",
            "type": "string",
        },
        {
            "property": "founded_on",
            "field": "FOUNDED_ON",
            "type": "string",
        },
        {
            "property": "email",
            "field": "EMAIL",
            "type": "string",
        },
        {
            "property": "employee_count",
            "field": "EMPLOYEE_COUNT",
            "type": "string",
        },
        {
            "property": "ipo_status",
            "field": "IPO_STATUS",
            "type": "string",
        }
    ],
    "merge_key": (("Organization",), {"property": "source_id", "field": "CRUNCHBASE_ORGANIZATION_UUID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

node = {
    "source": "cb_org_institutions",
    "labels": ("Organization", "Institution", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "INSTITUTION_UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "INSTITUTION_NAME",
            "type": "string",
        }
    ],
    "merge_key": (("Organization",), {"property": "source_id", "field": "INSTITUTION_UUID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)




"""
URL nodes
"""

temp = [
    {"source": "ss_org", "field": "TWITTER", "label": "Twitter"},
    {"source": "ss_org", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "ss_org", "field": "FACEBOOK", "label": "Facebook"},
    {"source": "ss_org", "field": "DOMAIN", "label": "Domain"},
    {"source": "cb_org", "field": "TWITTER", "label": "Twitter"},
    {"source": "cb_org", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "cb_org", "field": "DOMAIN", "label": "Domain"},
    {"source": "ss_person", "field": "TWITTER", "label": "Twitter"},
    {"source": "ss_person", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "ss_person", "field": "FACEBOOK", "label": "Facebook"},
    {"source": "ss_person", "field": "WEBSITE", "label": "Website"},
    {"source": "cb_person", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "cb_person", "field": "TWITTER", "label": "Twitter"},
    {"source": "cb_person", "field": "FACEBOOK", "label": "Facebook"},
]

nodes = [
    {
        "source": x["source"],
        "labels": ("Url", x["label"]),
        "properties_list": [
            {
                "property": "url",
                "field": x["field"],
                "type": "string",
            },
        ],
        "merge_key": (("Url",), {"property": "url", "field": x["field"]}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
NODES.extend(nodes)

"""
Investor nodes
"""

node = {
    "source": "cb_investor_org",
    "labels": ("Investor", "Organization", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "CRUNCHBASE_INVESTOR_UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "INVESTOR_NAME",
            "type": "string",
        },
        {
            "property": "investor_type",
            "field": "INVESTOR_TYPES",
            "type": "string",
        },
        {
            "property": "founded_on",
            "field": "FOUNDED_ON",
            "type": "string",
        },
        {
            "property": "investment_count",
            "field": "INVESTMENT_COUNT",
            "type": "int",
        },
        {
            "property": "total_funding_usd",
            "field": "TOTAL_FUNDING_USD",
            "type": "float",
        }
    ],
    "merge_key": (("Investor",), {"property": "source_id", "field": "CRUNCHBASE_INVESTOR_UUID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

node = {
    "source": "cb_investor_person",
    "labels": ("Investor", "Person", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "CRUNCHBASE_INVESTOR_UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "INVESTOR_NAME",
            "type": "string",
        },
        {
            "property": "investor_type",
            "field": "INVESTOR_TYPES",
            "type": "string",
        },
        {
            "property": "investment_count",
            "field": "INVESTMENT_COUNT",
            "type": "integer",
        },
        {
            "property": "total_funding_usd",
            "field": "TOTAL_FUNDING_USD",
            "type": "float",
        }
    ],
    "merge_key": (("Investor",), {"property": "source_id", "field": "CRUNCHBASE_INVESTOR_UUID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

"""
Event nodes
"""
node = {
    "source": "cb_event",
    "labels": ("Event", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "EVENT_UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "EVENT_NAME",
            "type": "string",
        }
    ],
    "merge_key": (("Event",), {"property": "source_id", "field": "EVENT_UUID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

"""
Year
"""

temp = [
    {"source": "ss_org", "label": "Sourcescrub"},
    {"source": "cb_org", "label": "Crunchbase"},
]

nodes = [
    {
        "source": x["source"],
        "labels": ("Year", x["label"]),
        "properties_list": [
            {
                "property": "year",
                "field": "YEAR",
                "type": "integer",
            },
        ],
        "merge_key": (("Year",), {"property": "year", "field": "YEAR_FOUNDED"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
NODES.extend(nodes)

"""
Location nodes
"""

temp = [
    {"source": "ss_org", "field": ["ORGANIZATION_CITY", "ORGANIZATION_STATE_CODE", "ORGANIZATION_COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]},
    {"source": "cb_org", "field": ["ORGANIZATION_CITY", "ORGANIZATION_STATE_CODE", "ORGANIZATION_COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]},
    {"source": "ss_person", "field": ["CITY", "STATE_CODE", "COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]},
    {"source": "cb_person", "field": ["CITY", "STATE_CODE", "COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]},
    {"source": "cb_investor_person", "field": ["CITY", "REGION", "COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]},
    {"source": "cb_investor_org", "field": ["CITY", "REGION", "COUNTRY_CODE"],
     "node_label": ["City", "State", "Country"]}
]

nodes = [
    {"source": x["source"],
     "labels": ("Location", node_lab),
     "properties_list": [
         {
             "property": node_lab.lower(),
             "field": field_name,
             "type": "string",
         },
     ],
     "merge_key": (("Location",), {"property": node_lab.lower(), "field": field_name}),
     "batch_size_factor": 1.0,
     }
    for x in temp
    for node_lab, field_name in zip(x["node_label"], x["field"])
]

NODES.extend(nodes)

"""
Job nodes
"""

temp = [
    {"source": "ss_person_org", "label": "Sourcescrub"},
    {"source": "cb_person_org", "label": "Crunchbase"},
]

nodes = [
    {
        "source": x["source"],
        "labels": ("Job", x["label"]),
        "properties_list": [
            {
                "property": "matched_title",
                "field": "MATCHED_TITLE",
                "type": "string",
            },
        ],
        "merge_key": (("Job",), {"property": "matched_title", "field": "MATCHED_TITLE"}),
        "batch_size_factor": 1.0,
    }
    for x in temp
]
NODES.extend(nodes)

"""
Person nodes
"""

node = {
    "source": "ss_person",
    "labels": ("Person", "Sourcescrub"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "ID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "NAME",
            "type": "string",
        },
        {
            "property": "email",
            "field": "EMAIL",
            "type": "string",
        }
    ],
    "merge_key": (("Person",), {"property": "source_id", "field": "ID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

node = {
    "source": "cb_person",
    "labels": ("Person", "Crunchbase"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "UUID",
            "type": "string",
        },
        {
            "property": "name",
            "field": "NAME",
            "type": "string",
        },
        {
            "property": "gender",
            "field": "GENDER",
            "type": "string",
        },
        {
            "property": "num_event_appearances",
            "field": "NUM_EVENT_APPEARANCES",
            "type": "integer",
        },
        {
            "property": "num_investment",
            "field": "NUM_INVESTMENT",
            "type": "integer",
        },
        {
            "property": "num_jobs",
            "field": "NUM_JOBS",
            "type": "integer",
        },
    ],
    "merge_key": (("Person",), {"property": "source_id", "field": "UUID"}),
    "batch_size_factor": 1.0,
}

NODES.append(node)

"""
Industry
"""
node = {
    "source": "industry",
    "labels": ("Industry",),
    "properties_list": [],
    "merge_key": (("Industry",), {"property": "industry", "field": "INDUSTRY"}),
    "batch_size_factor": 1.0,
}


"""
Other organization attributes nodes
"""

"""
Fund nodes
"""
#%% md
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