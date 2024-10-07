from  datetime import datetime

YMD = "%Y-%m-%d"
MYD = "%m/%d/%Y"

def parsedate_mdy(text:str) -> datetime:
    return datetime.strptime(text, MYD)



def formatdate_ymd(date:datetime) -> str:
    return date.strftime(YMD)

if __name__ == "__main__":
     
    date = "12/30/1999"
    date_dt_expect = datetime(1999, 12, 30)
    data_dt_actual = parsedate_mdy(date)
    assert date_dt_expect == data_dt_actual


    def test_formatdate_ymd():
        date = datetime(1999, 12, 30)
        expect = "1999-12-30"
        actual = formatdate_ymd(date)
        assert expect == actual