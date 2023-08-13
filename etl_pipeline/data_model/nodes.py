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

