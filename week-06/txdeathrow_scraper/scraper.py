from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso


def get_inmate_data():
    """
    A convenient wrapper function that wraps up all the other sub/helper
        functions so that the user of the scraper.py script need only
        to invoke this to get the nice and clean data.

        import scraper
        data = scraper.get_data()

    Returns:
        <list>: A list of dict objects, with the dict objects as defined in
            the documentation of the wrangle_inmate_data_from_tag()
            function
    """
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data



def get_and_parse_inmate_rows():
    """
    A convenience function that calls the functions needed to
      fetch the webpage, parse it as HTML, and return a list of bs4 <Tag>
      objects, each one derived from the HTML for a table row
       that ostensibly contains info about a TX death row inmate

    Should call on functionality in the `data_helper.py` script (i.e. get_html())

    Args:
        None

    Returns:
        <list>: A list of bs4.Tag objects, of the <tr> type
    """
    txt=data_helper.get_html()
    soup=BeautifulSoup(txt,'lxml')
    tag=soup.select('tr')
    rows=[]
    for x in tag:
        rows.append(x)
    return rows[1:]

def wrangle_inmate_data_from_tag(rowtag):
    """
    Args:
        rowtag: a BeautifulSoup <Tag> object, ostensibly representing a table row
            from a parsed Texas death row HTML table, e.g.

            <tr>
            <td>999608</td>
            <td align="center"><a href="dr_info/hudsonwilliam.html" title="Offender Information for William Hudson">Offender Information</a></td>
            <td>Hudson</td>
            <td>William</td>
            <td>07/03/1982</td>
            <td align="center">M</td>
            <td>White</td>
            <td>11/16/2017</td>
            <td>Anderson</td>
            <td>11/14/2015</td>
            </tr>

    Returns:
        <dict>: A dictionary object that contains some of the values in
            the HTML, with formatting where standardization is needed --
            e.g. for dates and for the inmate's URL (absolute vs relative)
            and some derived attributes, e.g. 'age_at_offense'

            The value for 'url' should be an absolute URL, i.e. a valid
               URL on the Web, not a relative one.

            'birthdate', date_received', 'date_offense' should be in 'YYYY-MM-DD'
                format

            All values are strings except for:
               'age_at_offense', which is an integer derived from birthdate and
                                 date of offense

               'years_before_death_row', which is a float
                              (rounded to nearest tenth) derived
                              from date of offense and date received, i.e.
                              number of years between commission of crime and entering
                              death row.

        e.g.
            {
                'tdcj_id': '999608',
                'url': 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html',
                'last_name': 'Hudson',
                'first_name': 'William',
                'birthdate': '1982-07-03',
                'gender': 'M',
                'race': 'White',
                'date_received': '2017-11-16',
                'date_offense': '2015-11-14',
                'age_at_offence': 33,
                'years_before_death_row': 2.0
            }
    """
    d={}
    cols=rowtag.select('td')
    acols=rowtag.select('td a')
    d['tdcj_id']=cols[0].text.strip()
    href=acols[0].attrs['href']
    d['url']=make_absolute_url(href)
    d['first_name']=cols[3].text.strip()
    d['last_name']=cols[2].text.strip()
    datestr=cols[4].text.strip()
    d['birthdate']=txdate_to_iso(datestr)
    d['gender']=cols[5].text.strip()
    d['race']=cols[6].text.strip()
    datestr=cols[7].text.strip()
    d['date_received']=txdate_to_iso(datestr)
    d['county']=cols[8].text.strip()
    datestr=cols[-1].text.strip()
    d['date_offense']=txdate_to_iso(datestr)
    d['age_at_offense']=round(calc_years_diff(d['birthdate'], d['date_offense']))
    d['years_before_death_row']=calc_years_diff(d['date_offense'],d['date_received'])
    return d
