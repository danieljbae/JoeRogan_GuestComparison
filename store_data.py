import pandas as pd
import sqlite3


def database_insert(db_filename,table_name,df):
    """
    Stores dataframe values into a databse file
    """

    # Storing in Database file 
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Create table
    c.execute("""CREATE TABLE IF NOT EXISTS VIDEOS (guest_Names text, 
                                                show_Num text, 
                                                guestName_show text,
                                                video_views INTEGER,
                                                engagement_Factor REAL,
                                                upload_Year blob,
                                                upload_month_year blob,
                                                contraversyFactor REAL,
                                                appearences_rollingCount INTEGER,
                                                views_rollingSum INTEGER,
                                                engagementFactor_rollingAvg REAL
                                                )"""                                
                )

    conn.commit()

    # insert to db
    df.to_sql('VIDEOS', conn, if_exists='replace', index = False)
    return db_filename,table_name
    

def create_df(db_filename,table_name,showNums,guestNames,videos_views,engagementFactors,contraversyFactors,uploadDates):
    """
    Convert lists of youtube data into dataframe
    Creates metrics and Formats data to plot
    Call database function to store
    """
    
    
    df = pd.DataFrame()
    df['guest_Names'] = guestNames
    df['show_Num'] = showNums
    df["guestName_show"] = df["guest_Names"].astype(str) + " - #"+ df["show_Num"].astype(str)        
    df['video_views'] = videos_views
    df['engagement_Factor'] = engagementFactors
    df['upload_Date'] = uploadDates
    df['upload_Year'] = pd.DatetimeIndex(df['upload_Date']).year
    df['upload_month_year'] = pd.to_datetime(df['upload_Date']).dt.to_period('M').astype(str)   # extracting year and month (ex. 2015-12)
    
    df['contraversyFactor'] = contraversyFactors
    df = df[df['guest_Names'] != "No guest found"] # shows on channel that are not podcasts
    df = df.sort_values(by= "show_Num")

    n = len(guestNames)
    df['appearences_rollingCount'] = df.groupby('guest_Names')['guest_Names'].transform(lambda x: round(x.rolling(n, 1).count(),2))
    df['views_rollingSum'] = df.groupby('guest_Names')['video_views'].transform(lambda x: round(x.rolling(n, 1).sum(),2))
    df['engagementFactor_rollingAvg'] = df.groupby('guest_Names')['engagement_Factor'].transform(lambda x: round(x.rolling(n, 1).mean(),2))

    db_name = database_insert(db_filename,table_name,df)


    return df,db_name   