import json
import video_data
import format_data 
import plot_data


def main():
    guestStats = {}

    # Extract videos in "Uploads" playlist 
    channelID = "UCzQUP1qoWDoEbmsQxvdjxgQ"
    showNums,guestNames,videos_ID,videos_views,engagementFactors,uploadDates = video_data.channelPlaylist(channelID)
    
    df = format_data.create_df(showNums,guestNames,videos_views,engagementFactors,uploadDates)
    # print(df.head())
    plot_data.create_dashboard(df)
    


if __name__ == "__main__":
    main()   