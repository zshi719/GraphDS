import pandas as pd

from etl.utils import (
    get_fields_for_source,
    get_df_from_snowflake,
    save_df_to_csv,
    standardize_url,
    standardize_city,
    standardize_state,
    standardize_country,
    standardize_job_title,
    get_df_for_industry,
    standardize_ss_industry,
    standardize_cb_industry,
    reduce_industry_df
)

source = "cb_acquisition"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_investor_investment"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_investor_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_investor_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)


source = "cb_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["ORGANIZATION_CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["ORGANIZATION_STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["ORGANIZATION_COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_org_institutions"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_parent"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_person_degree"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_person_to_org_current"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "cb_person_to_org_former"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "ss_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["ORGANIZATION_CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["ORGANIZATION_STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["ORGANIZATION_COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "ss_parent"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "ss_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["WEBSITE"] = df["WEBSITE"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "ss_person_to_org_current"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "ss_person_to_org_former"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "industry"
df = get_df_for_industry()
save_df_to_csv(df, source=source)

source = "ss_org_industry"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: standardize_ss_industry(x))
df = df.explode("INDUSTRY")
df.drop_duplicates(inplace = True, ignore_index = True)
df = reduce_industry_df(df, "INDUSTRY")
save_df_to_csv(df, source=source)


source = "cb_org_industry"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: x.split(","))
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: standardize_cb_industry(x))
df = df.explode("INDUSTRY")
df.drop_duplicates(inplace = True, ignore_index = True)
df = reduce_industry_df(df, "INDUSTRY")
save_df_to_csv(df, source=source)