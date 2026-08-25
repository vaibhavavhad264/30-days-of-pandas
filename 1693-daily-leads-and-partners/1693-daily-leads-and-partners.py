# 25/08/2026
import pandas as pd

def daily_leads_and_partners(daily: pd.DataFrame) -> pd.DataFrame:
    return (
        daily.groupby(['date_id', 'make_name'])
        .agg(
            unique_leads=('lead_id', 'nunique'),
            unique_partners=('partner_id', 'nunique')
        )
        .reset_index()
    )