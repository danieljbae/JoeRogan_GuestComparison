import pandas as pd


def create_df(showNums,guestNames,videos_views,engagementFactors,uploadDates):
    n = len(guestNames)
    df = pd.DataFrame()
    df['guest_Names'] = guestNames
    df['show_Num'] = showNums
    df['video_views'] = videos_views
    df['engagement_Factor'] = engagementFactors
    df['upload_Date'] = uploadDates
    df['upload_Year'] = pd.DatetimeIndex(df['upload_Date']).year


    df = df[df['guest_Names'] != "No guest found"] 
    df = df.sort_values(by= "show_Num")

    df['appearences_rollingCount'] = df.groupby('guest_Names')['guest_Names'].transform(lambda x: round(x.rolling(n, 1).count(),2))
    df['views_rollingAvg'] = df.groupby('guest_Names')['video_views'].transform(lambda x: round(x.rolling(n, 1).sum(),2))
    df['engagementFactor_rollingAvg'] = df.groupby('guest_Names')['engagement_Factor'].transform(lambda x: round(x.rolling(n, 1).mean(),2))




    return df