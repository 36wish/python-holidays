# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta as rd, FR, SA, MO

from holidays.constants import JAN, APR, MAY, SEP
from holidays.constants import SAT, SUN
from holidays.holiday_base import HolidayBase


class Vietnam(HolidayBase):

    # https://publicholidays.vn/
    # http://vbpl.vn/TW/Pages/vbpqen-toanvan.aspx?ItemID=11013 Article.115
    # https://www.timeanddate.com/holidays/vietnam/

    def __init__(self, **kwargs):
        self.country = "VN"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        name = "International New Year's Day"
        first_date = date(year, JAN, 1)
        self[first_date] = name
        if self.observed:
            self[first_date] = name
            if first_date.weekday() == SAT:
                self[first_date + rd(days=+2)] = name + " observed"
            elif first_date.weekday() == SUN:
                self[first_date + rd(days=+1)] = name + " observed"

        # Lunar New Year
        name = ["Vietnamese New Year",           # index: 0
                "The second day of Tet Holiday",  # index: 1
                "The third day of Tet Holiday",  # index: 2
                "The forth day of Tet Holiday",  # index: 3
                "The fifth day of Tet Holiday",  # index: 4
                "Vietnamese New Year's Eve",     # index: -1
                ]
        dt = self.get_solar_date(year, 1, 1)
        new_year_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            for i in range(-1, 5, 1):
                tet_day = new_year_date + rd(days=+i)
                self[tet_day] = name[i]

        # Vietnamese Kings' Commemoration Day
        # https://en.wikipedia.org/wiki/H%C3%B9ng_Kings%27_Festival
        if year >= 2007:
            name = "Hung Kings Commemoration Day"
            dt = self.get_solar_date(year, 3, 10)
            king_hung_date = date(dt.year, dt.month, dt.day)
            self[king_hung_date] = name
        else:
            pass

        # Liberation Day/Reunification Day
        name = "Liberation Day/Reunification Day"
        libration_date = date(year, APR, 30)
        self[libration_date] = name

        # International Labor Day
        name = "International Labor Day"
        labor_date = date(year, MAY, 1)
        self[labor_date] = name

        # Independence Day
        name = "Independence Day"
        independence_date = date(year, SEP, 2)
        self[independence_date] = name

    # Store the number of days per year from 1901 to 2099, and the number of
    # days from the 1st to the 13th to store the monthly (including the month
    # of the month), 1 means that the month is 30 days. 0 means the month is
    # 29 days. The 12th to 15th digits indicate the month of the next month.
    # If it is 0x0F, it means that there is no leap month.
    g_lunar_month_days = [
        0xF0EA4, 0xF1D4A, 0x52C94, 0xF0C96, 0xF1536,
        0x42AAC, 0xF0AD4, 0xF16B2, 0x22EA4, 0xF0EA4,  # 1901-1910
        0x6364A, 0xF164A, 0xF1496, 0x52956, 0xF055A,
        0xF0AD6, 0x216D2, 0xF1B52, 0x73B24, 0xF1D24,  # 1911-1920
        0xF1A4A, 0x5349A, 0xF14AC, 0xF056C, 0x42B6A,
        0xF0DA8, 0xF1D52, 0x23D24, 0xF1D24, 0x61A4C,  # 1921-1930
        0xF0A56, 0xF14AE, 0x5256C, 0xF16B4, 0xF0DA8,
        0x31D92, 0xF0E92, 0x72D26, 0xF1526, 0xF0A56,  # 1931-1940
        0x614B6, 0xF155A, 0xF0AD4, 0x436AA, 0xF1748,
        0xF1692, 0x23526, 0xF152A, 0x72A5A, 0xF0A6C,  # 1941-1950
        0xF155A, 0x52B54, 0xF0B64, 0xF1B4A, 0x33A94,
        0xF1A94, 0x8152A, 0xF152E, 0xF0AAC, 0x6156A,  # 1951-1960
        0xF15AA, 0xF0DA4, 0x41D4A, 0xF1D4A, 0xF0C94,
        0x3192E, 0xF1536, 0x72AB4, 0xF0AD4, 0xF16D2,  # 1961-1970
        0x52EA4, 0xF16A4, 0xF164A, 0x42C96, 0xF1496,
        0x82956, 0xF055A, 0xF0ADA, 0x616D2, 0xF1B52,  # 1971-1980
        0xF1B24, 0x43A4A, 0xF1A4A, 0xA349A, 0xF14AC,
        0xF056C, 0x60B6A, 0xF0DAA, 0xF1D92, 0x53D24,  # 1981-1990
        0xF1D24, 0xF1A4C, 0x314AC, 0xF14AE, 0x829AC,
        0xF06B4, 0xF0DAA, 0x52D92, 0xF0E92, 0xF0D26,  # 1991-2000
        0x42A56, 0xF0A56, 0xF14B6, 0x22AB4, 0xF0AD4,
        0x736AA, 0xF1748, 0xF1692, 0x53526, 0xF152A,  # 2001-2010
        0xF0A5A, 0x4155A, 0xF156A, 0x92B54, 0xF0BA4,
        0xF1B4A, 0x63A94, 0xF1A94, 0xF192A, 0x42A5C,  # 2011-2020
        0xF0AAC, 0xF156A, 0x22B64, 0xF0DA4, 0x61D52,
        0xF0E4A, 0xF0C96, 0x5192E, 0xF1956, 0xF0AB4,  # 2021-2030
        0x315AC, 0xF16D2, 0xB2EA4, 0xF16A4, 0xF164A,
        0x63496, 0xF1496, 0xF0956, 0x50AB6, 0xF0B5A,  # 2031-2040
        0xF16D4, 0x236A4, 0xF1B24, 0x73A4A, 0xF1A4A,
        0xF14AA, 0x5295A, 0xF096C, 0xF0B6A, 0x31B54,  # 2041-2050
        0xF1D92, 0x83D24, 0xF1D24, 0xF1A4C, 0x614AC,
        0xF14AE, 0xF09AC, 0x40DAA, 0xF0EAA, 0xF0E92,  # 2051-2060
        0x31D26, 0xF0D26, 0x72A56, 0xF0A56, 0xF14B6,
        0x52AB4, 0xF0AD4, 0xF16CA, 0x42E94, 0xF1694,  # 2061-2070
        0x8352A, 0xF152A, 0xF0A5A, 0x6155A, 0xF156A,
        0xF0B54, 0x4174A, 0xF1B4A, 0xF1A94, 0x3392A,  # 2071-2080
        0xF192C, 0x7329C, 0xF0AAC, 0xF156A, 0x52B64,
        0xF0DA4, 0xF1D4A, 0x41C94, 0xF0C96, 0x8192E,  # 2081-2090
        0xF0956, 0xF0AB6, 0x615AC, 0xF16D4, 0xF0EA4,
        0x42E4A, 0xF164A, 0xF1516, 0x22936,           # 2090-2099
    ]
    # Define range of years
    START_YEAR, END_YEAR = 1901, 1900 + len(g_lunar_month_days)
    # 1901 The 1st day of the 1st month of the Gregorian calendar is 1901/2/19
    LUNAR_START_DATE, SOLAR_START_DATE = (1901, 1, 1), datetime(1901, 2, 19)
    # The Gregorian date for December 30, 2099 is 2100/2/8
    LUNAR_END_DATE, SOLAR_END_DATE = (2099, 12, 30), datetime(2100, 2, 18)

    def get_leap_month(self, lunar_year):
        return (self.g_lunar_month_days[lunar_year - self.START_YEAR] >> 16) \
            & 0x0F

    def lunar_month_days(self, lunar_year, lunar_month):
        return 29 + ((self.g_lunar_month_days[lunar_year - self.START_YEAR] >>
                      lunar_month) & 0x01)

    def lunar_year_days(self, year):
        days = 0
        months_day = self.g_lunar_month_days[year - self.START_YEAR]
        for i in range(1, 13 if self.get_leap_month(year) == 0x0F else 14):
            day = 29 + ((months_day >> i) & 0x01)
            days += day
        return days

    # Calculate the Gregorian date according to the lunar calendar
    def get_solar_date(self, year, month, day):
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self.lunar_year_days(y)
        leap_month = self.get_leap_month(year)
        for m in range(1, month + (month > leap_month)):
            span_days += self.lunar_month_days(year, m)
        span_days += day - 1
        return self.SOLAR_START_DATE + timedelta(span_days)


class VN(Vietnam):
    pass
