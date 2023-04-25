import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Cities, months and days for filters 
cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("Hello! Let's explore some US bikeshare data!")
    
    # Get user input for city (Chicago, New York, Washington). Use a while loop to handle invalid inputs.
    while True:
        city =input("Which city would you like to see? :\n Chicago, New York, or Washington\n").lower()
        if city in cities:
            break
        else:
            print('Sorry, Try again.')
            
    # Get filter by month, day, or no.
    while True:
        choice = input("Would you like to filter the data by month, day, or none?\n").lower()
        if choice == 'month':
            month = input("Please enter the month you want. Enter 'all' for no filter. \nChoices: All, January, February, March, April, May, June\n").lower()
            day = 'all'
            if month in months:
                break
            else:
                print('Sorry, Try again.')
        elif choice == 'day':
            day = input("Please enter the day of the week you want. Enter 'all' for no filter. \nChoices: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()
            month = 'all'
            if day in days:
                break
            else:
                print('Sorry, Try again.')
        elif choice == 'none':
            month = 'all'
            day = 'all'
            break
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
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all': 
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month from start time column to create month column 
    df['month'] = df['Start Time'].dt.month
    most_month = df['month'].mode()[0]
    
    # Alternative code option to simplify code
    
    '''
    #import calendar
    #most_month = calendar.month_name[most_month]
    '''
    
    # Change month to number
    if most_month == 1:
    most_month = "January"
elif most_month == 2:
    most_month = "February"
elif most_month == 3:
    most_month = "March"
elif most_month == 4:
    most_month = "April"
elif most_month == 5:
    most_month = "May"
elif most_month == 6:
    most_month = "June"
    print('Most Common Month: \n', most_month)
    
    # Display the most common day of the week
    most_day = df['day_of_week'].mode()[0] 
    print('The most common day of the week: \n', most_day) 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_starthour = df['hour'].mode()[0]
    print(f'"The most common start hour : {most_starthour}"')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s_staion = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station :', s_staion)

    # TO DO: display most commonly used end station
    e_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station :', e_station)

    # TO DO: display most frequent combination of start station and end station trip
    com_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    start_com_station = com_station.idxmax()[0]
    end_com_station = com_station.idxmax()[1]
    print('combination start station :' , start_com_station, end = '\n')
    print('combination end station :', end_com_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    print('total travel time :', trip_sum)

    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print('mean travel time : ', round(trip_mean, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types : ', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('Gender Types : ', gender_types)
    except KeyError:
      print("Gender Types: No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest = df['Birth Year'].min()
      print('earliest: ', earliest)
    except KeyError:
      print("earliest year: No data available for this month.")

    try:
      most_recent = df['Birth Year'].max()
      print('most recent:', most_recent)
    except KeyError:
      print("most recent year: No data available for this month.")

    try:
      most_common = df['Birth Year'].value_counts().idxmax()
      print('most common year:', most_common)
    except KeyError:
      print("most Common Year: No data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
