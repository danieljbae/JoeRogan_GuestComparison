import pandas as pd

def create_df(showNums,guestNames,videos_views,engagementFactors,contraversyFactors,uploadDates):
    df = pd.DataFrame()
    df['guest_Names'] = guestNames
    df['show_Num'] = showNums
    df["guestName_show"] = df["guest_Names"].astype(str) + " - #"+ df["show_Num"].astype(str)        
    df['video_views'] = videos_views
    df['engagement_Factor'] = engagementFactors
    df['upload_Date'] = uploadDates
    df['upload_Year'] = pd.DatetimeIndex(df['upload_Date']).year
    df['upload_month_year'] = pd.to_datetime(df['upload_Date']).dt.to_period('M') # extracting year and month (ex. 2015-12)
    
    df['contraversyFactor'] = contraversyFactors
    df = df[df['guest_Names'] != "No guest found"] # shows on channel that are not podcasts
    df = df.sort_values(by= "show_Num")

    n = len(guestNames)
    df['appearences_rollingCount'] = df.groupby('guest_Names')['guest_Names'].transform(lambda x: round(x.rolling(n, 1).count(),2))
    df['views_rollingSum'] = df.groupby('guest_Names')['video_views'].transform(lambda x: round(x.rolling(n, 1).sum(),2))
    df['engagementFactor_rollingAvg'] = df.groupby('guest_Names')['engagement_Factor'].transform(lambda x: round(x.rolling(n, 1).mean(),2))

    return df   