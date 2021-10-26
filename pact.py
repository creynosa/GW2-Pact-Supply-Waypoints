#!/usr/bin/env python3

from datetime import datetime, timezone

import pyperclip as pc

today = datetime.now(timezone.utc)
day = today.weekday()
hour = today.hour

chatcodes = {
    -1: "[&BIkHAAA=][&BDoBAAA=][&BO4CAAA=][&BC0AAAA=][&BIUCAAA=][&BCECAAA=]",
    0: "[&BIcHAAA=][&BEwDAAA=][&BNIEAAA=][&BKYBAAA=][&BIMCAAA=][&BA8CAAA=]",
    1: "[&BH8HAAA=][&BEgAAAA=][&BKgCAAA=][&BBkAAAA=][&BGQCAAA=][&BIMBAAA=]",
    2: "[&BH4HAAA=][&BMIBAAA=][&BP0CAAA=][&BKYAAAA=][&BDgDAAA=][&BPEBAAA=]",
    3: "[&BKsHAAA=][&BE8AAAA=][&BP0DAAA=][&BIMAAAA=][&BF0GAAA=][&BOcBAAA=]",
    4: "[&BJQHAAA=][&BMMCAAA=][&BJsCAAA=][&BNUGAAA=][&BHsBAAA=][&BNMAAAA=]",
    5: "[&BH8HAAA=][&BLkCAAA=][&BBEDAAA=][&BJIBAAA=][&BEICAAA=][&BBABAAA=]",
    6: "[&BIkHAAA=][&BDoBAAA=][&BO4CAAA=][&BC0AAAA=][&BIUCAAA=][&BCECAAA=]",
}

days = {
    -1: "Sunday",
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

if hour < 8:
    day = day - 1
text = chatcodes[day]

pc.copy(text)

print(f"Vendor Weekday Locations: {days[day]}")
print("Chatcodes copied successfully!\n")
