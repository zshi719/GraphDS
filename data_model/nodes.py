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
            "property": "founding_year",
            "field": "FOUNDING_YEAR",
            "type": "int",
        },
        {
            "property": "city",
            "field": "ORGANIZATION_CITY",
            "type": "string",
        },
        {
            "property": "state",
            "field": "ORGANIZATION_STATE",
            "type": "string",
        },
        {
            "property": "postal_code",
            "field": "ORGANIZATION_POSTAL_CODE",
            "type": "int",
        },
        {
            "property": "country",
            "field": "ORGANIZATION_COUNTRY",
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
            "property": "city",
            "field": "ORGANIZATION_CITY",
            "type": "string",
        },
        {
            "property": "country",
            "field": "ORGANIZATION_COUNTRY_CODE",
            "type": "string",
        },
        {
            "property": "state",
            "field": "ORGANIZATION_STATE_CODE",
            "type": "string",
        },
        {
            "property": "email",
            "field": "EMAIL",
            "type": "string",
        },
        {
            "property": "company_type",
            "field": "COMPANY_TYPE",
            "type": "",
        },
        {
            "property": "founded_on",
            "field": "FOUNDED_ON",
            "type": "datetime",
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

"""
URL nodes
"""

temp = [
    {"source": "ss_org", "field": "TWITTER_URL", "label": "Twitter"},
    {"source": "ss_org", "field": "LINKEDIN_URL", "label": "Linkedin"},
    {"source": "ss_org", "field": "FACEBOOK_URL", "label": "Facebook"},
    {"source": "ss_org", "field": "DOMAIN", "label": "Domain"},
    {"source": "cb_org", "field": "TWITTER", "label": "Twitter"},
    {"source": "cb_org", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "cb_org", "field": "DOMAIN", "label": "Domain"},
    {"source": "graph_ss_person", "field": "TWITTER", "label": "Twitter"},
    {"source": "graph_ss_person", "field": "EMAIL", "label": "Email"},
    {"source": "graph_ss_person", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "graph_ss_person", "field": "FACEBOOK", "label": "Facebook"},
    {"source": "graph_ss_person", "field": "WEBSITE", "label": "Website"},
    {"source": "graph_cb_person", "field": "LINKEDIN", "label": "Linkedin"},
    {"source": "graph_cb_person", "field": "TWITTER", "label": "Twitter"},
    {"source": "graph_ss_person", "field": "FACEBOOK", "label": "Facebook"},
    {"source": "graph_cb_person", "field": "CHRUNCHBASE", "label": "Chrunchbase"},
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
Person nodes
"""

node = {
    "source": "graph_ss_person",
    "labels": ("Person", "Sourcescrub"),
    "properties_list": [
        {
            "property": "source_id",
            "field": "ID",
            "type": "string",
        },
        {
            "property": "city",
            "field": "CITY",
            "type": "string",
        },
        {
            "property": "state",
            "field": "STATE",
            "type": "string",
        },
        {
            "property": "country",
            "field": "COUNTRY",
            "type": "string",
        },
        {
            "property": "state_code",
            "field": "STATE_CODE",
            "type": "string",
        },
        {
            "property": "country_code",
            "field": "COUNTRY_CODE",
            "type": "string",
        },
        # Q: email was treated as a field of the organization instead of part of URL

    ],
    "merge_key": (("Person",), {"property": "source_id", "field": "ID"}),
    "batch_size_factor": 1.0,
}
NODES.append(node)

node = {
    "source": "graph_cb_person",
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
            "property": "city",
            "field": "CITY",
            "type": "string",
        },
        {
            "property": "state_code",
            "field": "STATE_CODE",
            "type": "string",
        },
        {
            "property": "region",
            "field": "REGION",
            "type": "string",
        },
        {
            "property": "country_code",
            "field": "COUNTRY_CODE",
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
