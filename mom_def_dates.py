# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:54:55 2020

@author: User
"""

"""
import mom_def_dates
mom_def_dates.dates()
now = mom_def_dates.now

import mom_def_dates
mom_def_dates.dates()
now = mom_def_dates.now
today = mom_def_dates.today
today1 = mom_def_dates.today1
yesterday = mom_def_dates.yesterday
yesterday1 = mom_def_dates.yesterday1
tomorrow = mom_def_dates.tomorrow
tomorrow1 = mom_def_dates.tomorrow1
time = mom_def_dates.time
day = mom_def_dates.day
day1 = mom_def_dates.day1

"""

def dates():
    #eg for Sunday 10th May 2020 :
    #TODAY
    global today                         #2020-05-10                     <class 'datetime.date'>
    global today1                        #2020-05-10                     <class 'str'>
    global today2                        #2020-02-03 21:59:34            <class 'str'>
    global day                           #Sunday                         <class 'datetime.date'>
    global day1                          #Sunday                         <class 'str'>
    global day_short                     #Sunday                         <class 'str'>
    global now                           #2020-05-10 10:38:50.244205     <class 'datetime.datetime'>
    global time                          #10:38                          <class 'str'>
    global time_now                      #(18, 35, 1, 543665)            <class 'datetime.time'>


    global ukdate_today                  #10 May                         <class 'str'>
    global ukdate                        #09 May 2020                    <class 'str'>
    global ukdate_slash                  #21/02/2020                     <class 'str'>
    global weekno                        #07                             <class 'int'>  # Mon = 0, Tue = 1, Wed = 2, Thurs = 3, Fri - 4, Sat =5, Sun = 6
    global time_less_four_hours          #07:11:02                       <class 'str'>
    global hour_less_four_hours          #08                             <class 'str'>
    global hour                          #12                             <class 'str'>
    global uk_day_date                   #Friday 07 June                 <class 'str'>'
    
    #YESTERDAY
    global yesterday                     #2020-05-09                     <class 'datetime.date'>
    global yesterday1                    #2020-05-09                     <class 'str'>
    global yesterday_day                 #Saturday                       <class 'datetime.date'>
    global yesterday_day1                #Saturday                       <class 'str>
    global uk_yesterday_date_long        #09 May 2020                    <class 'str'>
    global ukdate_yesterday              #09 May                         <class 'str'>
    
    #DAY BEFORE YESTERDAY
    global date_two_days_ago             #2020-05-08                     <class 'datetime.date'>
    global date_two_days_ago1            #2020-05-08                     <class 'str'>
    global two_days_ago_day              #Friday                         <class 'datetime.date'>
    global two_days_ago_day1             #Friday                         <class 'str'>
    global uk_two_days_ago_date_long     #08 May 2020                    <class 'str'>
    global ukdate_day_before_yesterday   #08 May                         <class 'str'>
    
    #TOMORROW
    global tomorrow                      #2020-05-11                     <class 'datetime.date'>
    global tomorrow1                     #2020-05-11                     <class 'str'>
    global tomorrow_day                  #Monday                         <class 'datetime.date'>
    global tomorrow_day1                 #Monday                         <class 'str'>
    global uk_tomorrow_date_long         #10 May 2020                    <class 'str'>
    
    #THREE DAYS AGO
    global date_three_days_ago           #2020-05-07                     <class 'datetime.date'>
    global date_three_days_ago1          #2020-05-07                     <class 'str'>
    global three_days_ago_day            #Thursday                       <class 'datetime.date'>
    global three_days_ago_day1           #Thursday                       <class 'str'>
    global uk_three_days_ago_date_long   #07 May 2020                    <class 'str'>
    
    #FOUR DAYS AGO
    global date_four_days_ago            #2020-05-07                     <class 'datetime.date'>
    global date_four_days_ago1           #2020-05-07                     <class 'str'>
    
    global current_month                #11                             <class 'int'>
    global current_month_short          #Nov                            <class 'str'>
    global current_month_long           #November                       <class 'str'>
    global current_second               #29                             <class 'int'>
    global current_minute               #24                             <class 'int'>
    global current_hour                 #12                             <class 'int'>
    
    global current_day                  #16                             <class 'int'>
    global current_year                 #2020                           <class 'int'>
    
    import datetime
    #today
    today = datetime.date.today()
    today1 = datetime.date.today().strftime("%Y-%m-%d")
    today2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day = today.strftime("%A")
    day1 = str(day)
    day_short = today.strftime("%a")
    
    #yesterday
    yesterday = today - datetime.timedelta(days = 1)
    yesterday1 = yesterday.strftime("%Y-%m-%d")
    yesterday_day = yesterday.strftime("%A")
    yesterday_day1 = str(yesterday_day)
    
    #day before yesterday
    date_two_days_ago = today - datetime.timedelta(days = 2)
    date_two_days_ago1 = date_two_days_ago.strftime("%Y-%m-%d")
    two_days_ago_day = date_two_days_ago.strftime('%A')
    two_days_ago_day1 = str(two_days_ago_day)
    
    #three days ago
    date_three_days_ago = today - datetime.timedelta(days = 3)
    date_three_days_ago1 = date_three_days_ago.strftime("%Y-%m-%d")
    three_days_ago_day = date_three_days_ago.strftime('%A')
    three_days_ago_day1 = str(three_days_ago_day)
    
    #four days ago
    date_four_days_ago = today - datetime.timedelta(days = 4)
    date_four_days_ago1 = str(date_four_days_ago)
    
    #tomorrow
    tomorrow = today + datetime.timedelta(days = 1)
    tomorrow1 = tomorrow.strftime("%Y-%m-%d")
    tomorrow_day = tomorrow.strftime('%A')
    tomorrow_day1 = str(tomorrow_day)
    
    #Day of week (useful for determining if is the weekend or not)
    weekno = datetime.datetime.today().weekday()
    
    
    
    
    #nice formats
    from datetime import datetime, timedelta
    uk_yesterday_date_long = datetime.strptime(f'{yesterday}', "%Y-%m-%d").strftime("%d %B %Y")
    now = datetime.now()
    time = now.strftime("%H:%M")
    time_now = datetime.now().time()
    hour = now.strftime("%H")
    time_less_four_hours = (datetime.now() - timedelta(hours = 4)).strftime('%H:%M:%S')
    hour_less_four_hours = (datetime.now() - timedelta(hours = 4)).strftime('%H')
    ukdate_today = datetime.strptime(f'{today}', "%Y-%m-%d").strftime("%d %b") 
    ukdate = datetime.strptime(f'{today}', "%Y-%m-%d").strftime("%d %b %Y")
    ukdate_slash = datetime.strptime(f'{today}', "%Y-%m-%d").strftime("%d/%m/%Y")
    ukdate_yesterday = datetime.strptime(f'{yesterday}', "%Y-%m-%d").strftime("%d %b")
    ukdate_day_before_yesterday = datetime.strptime(f'{date_three_days_ago}', "%Y-%m-%d").strftime("%d %b")
    uk_two_days_ago_date_long = datetime.strptime(f'{date_two_days_ago}', "%Y-%m-%d").strftime("%d %B %Y")
    uk_three_days_ago_date_long = datetime.strptime(f'{date_three_days_ago}', "%Y-%m-%d").strftime("%d %B %Y")
    uk_tomorrow_date_long = datetime.strptime(f'{tomorrow}', "%Y-%m-%d").strftime("%d %B %Y")
    uk_day_date = datetime.strptime(f'{today}', "%Y-%m-%d").strftime("%a %d %B")
    
    #current month
    current_second= datetime.now().second
    current_minute = datetime.now().minute
    current_hour = datetime.now().hour
    
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    current_month_short = datetime.now().strftime("%b")
    current_month_long = datetime.now().strftime("%B")
    

    
