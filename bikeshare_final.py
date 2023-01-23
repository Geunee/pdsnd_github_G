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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_input = input('''
        Which city do you want filter by?
        
        1. CHICAGO
        2. NEW_YORK_CITY
        3. WASHINGTON

        Plese input city's number

        ''')
        
        city = int(city_input)

        if city not in (1, 2, 3):
            print('Sorry, Try again')
            continue
        else:
            if city == 1:
                city = 'chicago'
            elif city == 2:
                city = 'new york city'
            elif city == 3:
                city = 'washington'
            
            print(f'"The city which you want is {city} "')
            break
    

        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input('''
        Which month do you want filter by?
        
        1. all
        2. January
        3. February
        4. March
        5. April
        6. May
        7. June
        
        Plese input month's number

        ''')
        
        month = int(month_input)

        if month not in (1, 2, 3, 4, 5, 6, 7):
            print('Sorry, Try again')
            continue
        else:
            if month == 1:
                month = 'all'
            elif month == 2:
                month = 'January'
            elif month == 3:
                month = 'February'
            elif month == 4:
                month = 'March'
            elif month == 5:
                month = 'April'
            elif month == 6:
                month = "May"
            elif month == 7:
                month = "June"
                    
            
            print(f'"The month which you want is {month} "')
            break


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('''
        Which day do you want filter by?
        
        1. all
        2. monday
        3. tuesday
        4. wednesday
        5. thursday
        6. friday
        7. saturday
        8. sunday
        
        Plese input day's number

        ''')
        
        day = int(day_input)

        if day not in (1, 2, 3, 4, 5, 6, 7, 8):
            print('Sorry, Try again')
            continue
        else:
            if day == 1:
                day = 'all'
            elif day == 2:
                day = 'monday'
            elif day == 3:
                day = 'tuesday'
            elif day == 4:
                day = 'wednesday'
            elif day == 5:
                day = 'thursday'
            elif day == 6:
                day = "saturday"
            elif day == 7:
                day = "sunday"
                    
            
            print(f'"The day which you want is {day} "')
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    # TO DO: display the most common month
    try:
        most_mon = df['month'].mode()[0]
        print(f'"The most common month : {most_mon}"')
    except KeyError:
        print("no data")

    # TO DO: display the most common day of week
    try:
        most_day = df['day_of_week'].mode()[0]
        print("The most common day of week :", most_day)
    except KeyError:
        print('no data')

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
    print('user_types : ', user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('gender_types : ', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earlist = df['Birth Year'].min()
    print('earliest :', int(earlist))

    most_recent = df['Birth Year'].max()
    print('most recent :', int(most_recent))

    most_common = df['Birth Year'].mode()
    print('most common :', int(most_common))

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
