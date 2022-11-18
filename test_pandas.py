import pandas as pd

df = pd.DataFrame({
    'customer_id': [1, 2, 3,
                    1, 2, 3,
                    1, 2, 3,
                    1, 2, 3,
                    1, 2, 3],
    'timestamp': pd.to_datetime(['2017-02-14 06:00:00', '2017-02-14 06:20:00', '2017-02-14 06:07:00',
                                 '2017-02-14 06:05:00', '2017-02-14 06:21:00', '2017-02-14 06:15:00',
                                 '2017-02-14 06:07:00', '2017-02-14 06:25:00', '2017-02-14 06:19:00',
                                 '2017-02-14 06:12:00', '2017-02-14 06:28:00', '2017-02-14 06:45:00',
                                 '2017-02-14 06:18:00', '2017-02-14 06:35:00', '2017-02-14 06:46:00'])
})

customers = df['customer_id'].unique().tolist()
for customer in customers:
    mask = df['customer_id'] == customer
    session_change_list = df.loc[mask, 'timestamp'].diff().dt.total_seconds() > 180
    session_id_list = []
    session_count = 0
    for session_change in session_change_list.tolist():
        session_count = session_count + 1 if session_change else session_count
        session_id_list.append(session_count)
    df.loc[mask, 'session_id'] = pd.Series(session_id_list, index=df.loc[mask].index, dtype=object)
