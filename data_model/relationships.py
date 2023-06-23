RELATIONSHIPS = []

"""
HAS_URL
"""
temp = [
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "TWITTER_URL"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "LINKEDIN_URL"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "FACEBOOK_URL"},
    {"source": "ss_org", "start_node_field": "SS_ID", "end_node_field": "DOMAIN"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "TWITTER_URL"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "LINKEDIN_URL"},
    {"source": "cb_org", "start_node_field": "CRUNCHBASE_ORGANIZATION_UUID", "end_node_field": "DOMAIN"},
    {"source": "graph_ss_person", "start_node_field": "ID", "end_node_field": "LINKEDIN"},
    {"source": "graph_ss_person", "start_node_field": "ID", "end_node_field": "TWITTER"},
    {"source": "graph_ss_person", "start_node_field": "ID", "end_node_field": "FACEBOOK"},
    {"source": "graph_ss_person", "start_node_field": "ID", "end_node_field": "LINKEDIN"},
    {"source": "graph_ss_person", "start_node_field": "ID", "end_node_field": "EMAIL"},
    {"source": "graph_cb_person", "start_node_field": "UUID", "end_node_field": "LINKEDIN"},
    {"source": "graph_cb_person", "start_node_field": "UUID", "end_node_field": "TWITTER"},
    {"source": "graph_cb_person", "start_node_field": "UUID", "end_node_field": "FACEBOOK"},
    {"source": "graph_cb_person", "start_node_field": "UUID", "end_node_field": "WEBSITE"},
    {"source": "graph_cb_person", "start_node_field": "UUID", "end_node_field": "CRUNCHBASE"}
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


"""
PARENT_OF
"""

relationship = {
    "source": "cb_parent",
    "properties_list": [],
    "merge_key": ("PARENT_OF",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "CB_PARENT_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "CB_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


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
        {
            "property": "uuid",
            "field": "UUID",
            "type": "string",
        }
    ],
    "merge_key": ("ACQUIRED_BY",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ACQUIRER_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "ACQUIREE_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


"""
ATTENDED_EVENT
"""

relationship = {
    "source": "cb_event",
    "properties_list": [
        {
            "property": "appearance_type",
            "field": "APPEARANCE_TYPE",
            "type": "string",
        }
    ],
    "merge_key": ("ATTENDED_EVENT",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "EVENT_UUID"}),
    "end_node_key": (("Organization",), {"property": "source_id", "field": "PARTICIPANT_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)




"""
CURRENT EMPLOYMENT
"""

relationship = {
    "source": "GRAPH_SS_PERSON_TO_ORG_CURRENT",
    "properties_list": [
        {"property": "start_date",
         "field": "START_DATE",
         "type": "string"},
        {"property": "title",
         "field": "TITLE",
         "type": "string"},
        {"property": "num_roles",
         "field": "NUM_ROLES",
         "type": "integer"},
    ],
    "merge_key": ("CURRENT_EMPLOYMENT",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "COMPANY_ID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_ID"}),
    "batch_size_factor": 1.0,
}

RELATIONSHIPS.append(relationship)

relationship = {
    "source": "GRAPH_CB_PERSON_TO_ORG_CURRENT",
    "properties_list": [
        {"property": "start_date",
         "field": "START_DATE",
         "type": "string"},
        {"property": "title",
         "field": "TITLE",
         "type": "string"},
        {"property": "job_type",
         "field": "JOB_TYPE",
         "type": "string"},
    ],
    "merge_key": ("CURRENT_EMPLOYMENT",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


"""
FORMER EMPLOYMENT
"""

relationship = {
    "source": "GRAPH_SS_PERSON_TO_ORG_FORMER",
    "properties_list": [
        {"property": "start_date",
         "field": "START_DATE",
         "type": "string"},
        {"property": "end_date",
         "field": "END_DATE",
         "type": "string"},
        {"property": "title",
         "field": "TITLE",
         "type": "string"},
        {"property": "num_roles",
         "field": "NUM_ROLES",
         "type": "integer"},
    ],
    "merge_key": ("FORMER_EMPLOYMENT",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "COMPANY_ID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_ID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


relationship = {
    "source": "GRAPH_CB_PERSON_TO_ORG_FORMER ",
    "properties_list": [
        {"property": "start_date",
         "field": "START_DATE",
         "type": "string"},
        {"property": "end_date",
         "field": "END_DATE",
         "type": "string"},
        {"property": "title",
         "field": "TITLE",
         "type": "string"},
        {"property": "type",
         "field": "JOB_TYPE",
         "type": "string"},
    ],
    "merge_key": ("FORMER_EMPLOYMENT",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "ORG_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


"""
PERSON_ATTENDED_EVENT
"""

relationship = {
    "source": "GRAPH_CB_EVENT_APPEAR_PERSON",
    "properties_list": [
        {
            "property": "appearance_type",
            "field": "APPEARANCE_TYPE",
            "type": "string",
        }
    ],
    "merge_key": ("PERSON_ATTENDED_EVENT",),
    "start_node_key": (("Event",), {"property": "source_id", "field": "EVENT_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PARTICIPANT_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)


"""
ATTENDED_SCHOOL
"""

relationship = {
    "source": "GRAPH_CB_PERSON_DEGREE",
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
            "type": "string",
        },
        {
            "property": "end_date",
            "field": "END_DATE",
            "type": "string",
        }
    ],
    "merge_key": ("ATTENDED_SCHOOL",),
    "start_node_key": (("Organization",), {"property": "source_id", "field": "INSTITUTION_UUID"}),
    "end_node_key": (("Person",), {"property": "source_id", "field": "PERSON_UUID"}),
    "batch_size_factor": 1.0,
}
RELATIONSHIPS.append(relationship)