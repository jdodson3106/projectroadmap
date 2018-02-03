from calendar import HTMLCalendar
import datetime

class ProjectCalendar(HTMLCalendar):

    def __init__(self, start_date, deadline):
        super(ProjectCalendar, self).__init__()
        self.start_date = start_date
        self.deadline = deadline
        self.calendardict = {}
        self.monthlist = []
        self.yearlist = []

    def is_single_year(self):
        if (self.deadline.year - self.start_date.year) > 0:
            return False
        else:
            return True

    def __check_valid_dates(self):
        deadlineYear = self.deadline.year
        startdateYear = self.start_date.year
        deadlineMonth = self.deadline.month
        startdateMonth = self.start_date.month

        if deadlineYear < startdateYear:
            raise ValueError("Deadline must be later than the start date.")
        elif deadlineYear == startdateYear and deadlineMonth < startdateMonth:
            raise ValueError("Deadline must be later than the start date.")
        else:
            pass

    def __start_year_months(self):
        startmonth = self.start_date.month
        startyearremainders = 12 - startmonth
        while startyearremainders >= 0:
            self.monthlist.append(startmonth)
            startmonth += 1
            startyearremainders -= 1

    def __end_year_premonths(self):
        endmonth = self.deadline.month
        premonthcounter = 1
        while premonthcounter <= endmonth:
            self.monthlist.append(premonthcounter)
            premonthcounter += 1


    def create_single_year_month_list(self):
        self.__check_valid_dates()
        if(self.deadline.month == self.start_date.month):
            self.monthlist.append(self.start_date.month)

        elif (self.deadline.month - self.start_date.month) >= 1:
            difference = self.deadline.month - self.start_date.month
            startmonth = self.start_date.month

            while difference >= 0:
                self.monthlist.append(startmonth)
                startmonth += 1
                difference -= 1


    def create_single_year_list(self):
        self.__check_valid_dates()
        if not self.is_single_year():
            raise ValueError("self.deadline.year is NOT equal to self.start_date.year")
        else:
            self.yearlist.append(self.deadline.year)


    def create_multiyear_month_list(self):
        self.__check_valid_dates()
        startyear = self.start_date.year
        endyear = self.deadline.year
        yeardifference = endyear - startyear

        #First, check for year equality and raise error
        if self.is_single_year():
            raise ValueError("self.deadline & self.start_date share the same year\n"
                             "Did you mean to call, object.create_single_year_month_list()?")

        # Second, compute for 12month revolving calendar (months are the same)
        elif yeardifference <= 1:
            self.__start_year_months()
            self.__end_year_premonths()

        # Third, compute the last edgecase, months don't match, to catch all
        # inbetween months
        elif yeardifference > 1:
            middlemonths = []
            monthcounter = 1
            while yeardifference > 1:
                while monthcounter <= 12:
                    middlemonths.append(monthcounter)
                    monthcounter += 1
                yeardifference -= 1
                monthcounter = 1

            self.__start_year_months()
            self.monthlist = self.monthlist + middlemonths
            self.__end_year_premonths()


    def create_multiyear_year_list(self):
        self.__check_valid_dates()
        if self.is_single_year():
            raise ValueError("self.deadline & self.start_date share the same year\n"
                             "Did you mean to call, object.create_single_year_list()?")
        else:
            yearsdifference = self.deadline.year - self.start_date.year
            year = self.start_date.year

            while yearsdifference >= 0:
                self.yearlist.append(year)
                year += 1
                yearsdifference -= 1


    def create_calendar_dict(self):
        # create variables to track the years and months
        startyear = self.start_date.year
        endyear = self.deadline.year
        startyear_months = 12 - self.start_date.month
        endmonths = self.deadline.month

        # firs if there is only one year, simply add the monthlist to the dict
        if self.is_single_year():
            self.create_single_year_month_list()
            self.create_single_year_list()
            for year in self.yearlist:
                for month in range(len(self.monthlist)):
                    self.calendardict[year] = self.monthlist

        # If there are multiple years, create multiyear and month lists
        # then create a year counter that is used to track the inbetween years
        # by subtracting 2 from the yearlist length (to ignore first year and last year in the list)
        # Then set currentyear to 1 to start calling the second index in the year list
        # then grab the current month.
        else:
            self.create_multiyear_year_list()
            self.create_multiyear_month_list()
            yearcounter = len(self.yearlist) - 2
            currentyear = 1
            currentmonth = startyear_months + 1
            # first add the first year and start year months list to the dict
            self.calendardict[startyear] = self.monthlist[:startyear_months + 1]

            # next, while the year counter > 0, add the current year index to the
            # calendardict with the list slice of startyearmonths -> current month
            # then increment the current year index counter, up the start months by 12
            # the current month up by 12, and decrement the year counter
            while yearcounter > 0:
                self.calendardict[self.yearlist[currentyear]] = self.monthlist[startyear_months + 1:currentmonth + 12]
                currentyear += 1
                startyear_months += 12
                currentmonth += 12
                yearcounter -= 1

            # finally, add the end year and the end of the monthlist items to the dict.
            self.calendardict[endyear] = self.monthlist[startyear_months + 1:]


    def get_calendar_dict(self):
        if not self.calendardict:
            raise ValueError('Calendar Dictionary is empty')
        return self.calendardict

    def create_calendar(self):
        htmlstring = ''
        for year in self.calendardict:
            for month in self.calendardict[year]:
                htmlstring += super(ProjectCalendar, self).formatmonth(year,month)
        return htmlstring
