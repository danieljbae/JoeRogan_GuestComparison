import video_data
import store_data 
import plot_data


def main():
     
    channelID = "UCzQUP1qoWDoEbmsQxvdjxgQ"  # podcaster's youtube channel
    table_name = 'VIDEOS'
    db_filename = 'videos.db'
    
    ## scrape youtube data 
    # showNums,guestNames,videos_ID,videos_views,engagementFactors,contraversyFactors,uploadDates = video_data.channelPlaylist(channelID)
    
    # format data and store data in database file
    # store_data.create_df(db_filename,table_name,showNums,guestNames,videos_views,engagementFactors,contraversyFactors,uploadDates)    
    
    
    
    # plot data from database file
    dfcolumn_names = ['guest_Names','show_Num','guestName_show','video_views','engagement_Factor',
            'upload_Date','upload_Year','upload_month_year','contraversyFactor',
            'appearences_rollingCount','views_rollingSum','engagementFactor_rollingAvg']
    
    plot_data.create_dashboard(db_filename,table_name,dfcolumn_names)  

if __name__ == "__main__":
    main()
       