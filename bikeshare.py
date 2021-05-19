import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    cities = ["chicago", "new york city", "washington"]
    city = input("Would you like to see bikeshare data for Chicago, New York City, or Washington?\n").lower()
    
    while city not in cities:
        city = input("Please select either Chicago, New York City, or Washington.\n").lower()
    
    month = "all"
    day = "all"
    time_filters = ["month", "day", "none"]
    filter_type = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter.\n").lower()
    
    while filter_type not in time_filters:
        filter_type = input("Sorry, I didn't catch that. Please select either month, day, or none as your time filter.\n").lower()
        
    if filter_type == "month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("Which month? January, February, March, April, May or June? Please type out the full month name.\n").lower()
        
        while month not in months:
            month = input("Sorry, I didn't catch that. Please select either January, February, March, April, May or June and type out the full month name.\n").lower()
    elif filter_type == "day":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type out the full day name.\n").title()
        
        while day not in days:
            day = input("Sorry, I didn't catch that.  Please select either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday and type out the full day name.\n").title()
        
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    month = months[most_common_month - 1].title()
    
    print("What is the most common month?")
    print(month)

    most_common_day = df['day_of_week'].mode()[0]
    print("What is the most common day of the week?")
    print(most_common_day)

    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("What is the most common start hour?")
    print(most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    print("What is the most commonly used start station?")
    print(most_common_start_station)

    most_common_end_station = df['End Station'].mode()[0]
    print("What is the most commonly used end station?")
    print(most_common_end_station)

    most_frequent = df.groupby(['colname1','colname2']).sum()
    
    print("What is the most frequent combination of start station and end station?")
    print(most_frequent)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("What is the total travel time?")
    print(total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print("What is the average travel time?")
    print(average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_user_types = df['User Type'].value_counts()
    print("What is the breakdown of users?")
    print(count_user_types)

    count_user_gender = "No data available" 
    
    if 'Gender' in df:
        count_user_gender = df['Gender'].value_counts()
        
    print("What is the breakdown of users by gender?")
    print(count_user_gender)

    print("What is the breakdown of users by birth year?")
    
    if 'Birth Year' in df:
        most_common = df['Birth Year'].mode()[0]
        most_recent = df['Birth Year'].max()
        earliest = df['Birth Year'].min()
        
        print("The earliest birth year is {}.\nThe most recent birth year is {}.\nThe most commong birth year is {}.".format(earliest, most_recent, most_common))
    else:
        print("No data available")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    print('\nAddiitonal options...\n')
    start_time = time.time()
    
    answer_options = ["yes", "no"]
    answer = input("Would you like to view the raw data?  Please type either 'yes' or 'no'\n").lower()
    
    while answer not in answer_options:
        answer = input("Sorry, I didn't catch that. Would you like to view raw data? Please type either 'yes' or 'no'.\n").lower()
    
    index_counter = 0
    
    while answer == "yes":
        print(df[index_counter: index_counter + 5])
        index_counter+=5
        
        answer = input("Do you want to see more data? Type either 'yes' or 'no'.\n").lower()
        
        while answer not in answer_options:
            input("Sorry, I didn't catch that. Would you like to view more raw data? Please select either 'yes' or 'no'.\n").lower()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()