import urllib
from urllib.parse import urljoin
from behave import given, when, then

@given(u'we want to add a disaster')
def user_on_disaster_newpage(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    print(base_url)
    open_url = urljoin(base_url,'/new')
    context.browser.get(open_url)


@when(u'we fill in the form')
def user_fills_in_the_form(context):
    # use print(context.browser.page_source) to aid debugging
    # only prints page source if there is an error in the step
    print(context.browser.page_source)
    disasterNo = context.browser.find_element('name', 'disasterNo')
    disasterNo.send_keys('2020-0055-WEF')

    year = context.browser.find_element('name', 'year')
    year.send_keys(2020)

    seq = context.browser.find_element('name', 'seq')
    seq.send_keys(15)

    group = context.browser.find_element('name', 'group')
    group.send_keys('"Natural')

    subgroup = context.browser.find_element('name', 'subgroup')
    subgroup.send_keys('A')

    type = context.browser.find_element('name', 'type')
    type.send_keys('Flood')

    subtype = context.browser.find_element('name', 'subtype')
    subtype.send_keys('')

    eventName = context.browser.find_element('name', 'eventName')
    eventName.send_keys('Ada')

    country = context.browser.find_element('name', 'eventName')
    country.send_keys('Bangladesh')

    iso = context.browser.find_element('name', 'iso')
    iso.send_keys('WEF')

    region = context.browser.find_element('name', 'region')
    region.send_keys('SouthernAsi')

    continent = context.browser.find_element('name', 'continent')
    continent.send_keys('Asia')

    location = context.browser.find_element('name', 'location')
    location.send_keys('Bangladesh')

    startYear = context.browser.find_element('name', 'startYear')
    startYear.send_keys('2020')

    startMonth = context.browser.find_element('name', 'startMonth')
    startMonth.send_keys('2')

    startDay = context.browser.find_element('name', 'startDay')
    startDay.send_keys('5')

    endYear = context.browser.find_element('name', 'endYear')
    endYear.send_keys('2020')

    endMonth = context.browser.find_element('name', 'endMonth')
    endMonth.send_keys('3')

    endDay = context.browser.find_element('name', 'endDay')
    endDay.send_keys('1')

    totalDeaths = context.browser.find_element('name', 'totalAffected')
    totalDeaths.send_keys('500')

    injured = context.browser.find_element('name', 'injured')
    injured.send_keys('200')

    affected = context.browser.find_element('name', 'affected')
    affected.send_keys('90000')

    totalAffected = context.browser.find_element('name', 'totalAffected')
    totalAffected.send_keys('23456')

    homeless = context.browser.find_element('name', 'homeless')
    homeless.send_keys('666')

    damageCost = context.browser.find_element('name', 'damageCost')
    damageCost.send_keys('7876')
    context.browser.find_element('name','submit').click()


@then(u'it succeeds')
def product_added(context):
    assert '2020-0055-WEF' in context.browser.page_source


@given(u'we have specific disasters to add')
def specific_disasters(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    open_url = urljoin(base_url,'/new')
    for row in context.table:
        context.browser.get(open_url)
        name_textfield = context.browser.find_element('name', 'disasterNo')
        name_textfield.send_keys(row['name'])
        price_textfield = context.browser.find_element('name','year')
        price_textfield.send_keys(row['year'])
        context.browser.find_element('name','submit').click()
        assert row['name'] in context.browser.page_source

@when(u'we visit the all page')
def step_impl(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    open_url = urljoin(base_url,'/all')
    context.browser.get(open_url)
    print(context.browser.page_source)
    assert 'Disaster Table' in context.browser.page_source

@then(u'we will find \'2020-0055-WEF\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we will find \'2020-0055-WEF\'')