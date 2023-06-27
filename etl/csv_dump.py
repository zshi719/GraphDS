from etl.utils import (
    get_fields_for_source,
    get_df_from_snowflake,
    save_df_to_csv,
    standardize_url,
    standardize_city,
    standardize_state,
    standardize_country,
)


source = "ss_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
# do transformations, if any
# standardize urls
df[""] = df[""].apply(lambda x: standardize_url(x, kind='linkedin'))
# standardize city name, state code, state name, country code, country name
df[""] = df[""].apply(lambda x: standardize_state(x, return_type="code"))
save_df_to_csv(df, source=source)


source = "cb_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
# do transformations, if any
# standardize urls
# standardize city name, state code, state name, country code, country name
save_df_to_csv(df, source=source)