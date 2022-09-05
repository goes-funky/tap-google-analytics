import json

from integrations_testing_framework import *
import tap_google_analytics
import os
import pytest

config_path = os.path.abspath('../sample_config.json')


# INFO: [ST | 05.09.2022] Using standard function in integrations_testing_framework caused a problem on schemas;
# it was selecting all the schemas anyway. Thus, I changed the code that way and generate the catalog only for
# the specified stream.
def select_schema(catalog_path: str, stream_name: str) -> str:
    """
    Creates a catalog file with the stream_name selected.
    Example: @with_sys_args(['--config', config_path, '--catalog', utils.select_schema('all-streams.json', 'epics')])

    :param str catalog_path: a path of a catalog
    :param str stream_name: the name of the stream to be modified
    :return: the path of the catalog created as string
    :rtype: str
    """
    f = open(catalog_path, "r")
    catalog = f.read()
    f.close()

    catalog = json.loads(catalog)
    cc = catalog.copy()

    for stream in catalog['streams']:
        if stream['stream'] == stream_name:
            stream['metadata'][0]['metadata']['selected'] = True
            cc['streams'] = [stream]
            break

    # Open the file for writing.
    f = open(f"catalogs/{stream_name}.json", "w")
    f.write(json.dumps(cc))
    f.close()

    return f"catalogs/{stream_name}.json"


# @pytest.mark.skip() # Currently failing due to a timezone issue
@assert_stdout_matches('all-streams.json')
@intercept_requests('requests/discovery.txt', generate=False)
# # @write_stdout('responses/discovery.txt', )
@with_sys_args(['--config', config_path, '--discover'])
def test_schema():
    tap_google_analytics.main()


@assert_stdout_matches('responses/website_overview.txt')
@intercept_requests('requests/website_overview.txt', generate=False)
# @write_stdout('responses/website_overview.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'website_overview')])
def test_website_overview():
    tap_google_analytics.main()


@assert_stdout_matches('responses/traffic_sources.txt')
@intercept_requests('requests/traffic_sources.txt', generate=False)
# @write_stdout('responses/traffic_sources.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'traffic_sources')])
def test_traffic_sources():
    tap_google_analytics.main()


@assert_stdout_matches('responses/traffic_sources_geo.txt')
@intercept_requests('requests/traffic_sources_geo.txt', generate=False)
# @write_stdout('responses/traffic_sources_geo.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'traffic_sources_geo')])
def test_traffic_sources_geo():
    tap_google_analytics.main()


@assert_stdout_matches('responses/revenue_sources.txt')
@intercept_requests('requests/revenue_sources.txt', generate=False)
# @write_stdout('responses/revenue_sources.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'revenue_sources')])
def test_revenue_sources():
    tap_google_analytics.main()


@assert_stdout_matches('responses/pages.txt')
@intercept_requests('requests/pages.txt', generate=False)
# @write_stdout('responses/pages.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'pages')])
def test_pages():
    tap_google_analytics.main()


@assert_stdout_matches('responses/locations.txt')
@intercept_requests('requests/locations.txt', generate=False)
# @write_stdout('responses/locations.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'locations')])
def test_locations():
    tap_google_analytics.main()


@assert_stdout_matches('responses/monthly_active_users.txt')
@intercept_requests('requests/monthly_active_users.txt', generate=False)
# @write_stdout('responses/monthly_active_users.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'monthly_active_users')])
def test_monthly_active_users():
    tap_google_analytics.main()


@assert_stdout_matches('responses/four_weekly_active_users.txt')
@intercept_requests('requests/four_weekly_active_users.txt', generate=False)
# @write_stdout('responses/four_weekly_active_users.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'four_weekly_active_users')])
def test_four_weekly_active_users():
    tap_google_analytics.main()


@assert_stdout_matches('responses/two_weekly_active_users.txt')
@intercept_requests('requests/two_weekly_active_users.txt', generate=False)
# @write_stdout('responses/two_weekly_active_users.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'two_weekly_active_users')])
def test_two_weekly_active_users():
    tap_google_analytics.main()


@assert_stdout_matches('responses/weekly_active_users.txt')
@intercept_requests('requests/weekly_active_users.txt', generate=False)
# @write_stdout('responses/weekly_active_users.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'weekly_active_users')])
def test_weekly_active_users():
    tap_google_analytics.main()


@assert_stdout_matches('responses/daily_active_users.txt')
@intercept_requests('requests/daily_active_users.txt', generate=False)
# @write_stdout('responses/daily_active_users.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'daily_active_users')])
def test_daily_active_users():
    tap_google_analytics.main()


@assert_stdout_matches('responses/devices.txt')
@intercept_requests('requests/devices.txt', generate=False)
# @write_stdout('responses/devices.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'devices')])
def test_devices():
    tap_google_analytics.main()


@assert_stdout_matches('responses/goal_conversions.txt')
@intercept_requests('requests/goal_conversions.txt', generate=False)
# @write_stdout('responses/goal_conversions.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'goal_conversions')])
def test_goal_conversions():
    tap_google_analytics.main()


@assert_stdout_matches('responses/goal_conversions1_10.txt')
@intercept_requests('requests/goal_conversions1_10.txt', generate=False)
# @write_stdout('responses/goal_conversions1_10.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'goal_conversions1_10')])
def test_goal_conversions1_10():
    tap_google_analytics.main()


@assert_stdout_matches('responses/goal_conversions11_20.txt')
@intercept_requests('requests/goal_conversions11_20.txt', generate=False)
# @write_stdout('responses/goal_conversions11_20.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'goal_conversions11_20')])
def test_goal_conversions11_20():
    tap_google_analytics.main()


@assert_stdout_matches('responses/goal_values1_10.txt')
@intercept_requests('requests/goal_values1_10.txt', generate=False)
# @write_stdout('responses/goal_values1_10.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'goal_values1_10')])
def test_goal_values1_10():
    tap_google_analytics.main()


@assert_stdout_matches('responses/goal_values11_20.txt')
@intercept_requests('requests/goal_values11_20.txt', generate=False)
# @write_stdout('responses/goal_values11_20.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'goal_values11_20')])
def test_goal_values11_20():
    tap_google_analytics.main()


@assert_stdout_matches('responses/campaign_adcontent_performance.txt')
@intercept_requests('requests/campaign_adcontent_performance.txt', generate=False)
# @write_stdout('responses/campaign_adcontent_performance.txt', )
@with_sys_args(
    ['--config', config_path, '--catalog', select_schema('all-streams.json', 'campaign_adcontent_performance')])
def test_campaign_adcontent_performance():
    tap_google_analytics.main()


@assert_stdout_matches('responses/campaign_adcontent_performance_v2.txt')
@intercept_requests('requests/campaign_adcontent_performance_v2.txt', generate=False)
# @write_stdout('responses/campaign_adcontent_performance_v2.txt', )
@with_sys_args(
    ['--config', config_path, '--catalog', select_schema('all-streams.json', 'campaign_adcontent_performance_v2')])
def test_campaign_adcontent_performance_v2():
    tap_google_analytics.main()


@assert_stdout_matches('responses/revenue_transactions.txt')
@intercept_requests('requests/revenue_transactions.txt', generate=False)
# @write_stdout('responses/revenue_transactions.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'revenue_transactions')])
def test_revenue_transactions():
    tap_google_analytics.main()


@assert_stdout_matches('responses/revenue_transactions_geo.txt')
@intercept_requests('requests/revenue_transactions_geo.txt', generate=False)
# @write_stdout('responses/revenue_transactions_geo.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'revenue_transactions_geo')])
def test_revenue_transactions_geo():
    tap_google_analytics.main()


@assert_stdout_matches('responses/page_flow_tracking.txt')
@intercept_requests('requests/page_flow_tracking.txt', generate=False)
# @write_stdout('responses/page_flow_tracking.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'page_flow_tracking')])
def test_page_flow_tracking():
    tap_google_analytics.main()


@assert_stdout_matches('responses/page_flow_tracking_geo.txt')
@intercept_requests('requests/page_flow_tracking_geo.txt', generate=False)
# @write_stdout('responses/page_flow_tracking_geo.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'page_flow_tracking_geo')])
def test_page_flow_tracking_geo():
    tap_google_analytics.main()


@assert_stdout_matches('responses/revenue_sources_geo.txt')
@intercept_requests('requests/revenue_sources_geo.txt', generate=False)
# @write_stdout('responses/revenue_sources_geo.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'revenue_sources_geo')])
def test_revenue_sources_geo():
    tap_google_analytics.main()


@assert_stdout_matches('responses/revenue_sources_utm.txt')
@intercept_requests('requests/revenue_sources_utm.txt', generate=False)
# @write_stdout('responses/revenue_sources_utm.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'revenue_sources_utm')])
def test_revenue_sources_utm():
    tap_google_analytics.main()


@assert_stdout_matches('responses/ecommerce_geo.txt')
@intercept_requests('requests/ecommerce_geo.txt', generate=False)
# @write_stdout('responses/ecommerce_geo.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'ecommerce_geo')])
def test_ecommerce_geo():
    tap_google_analytics.main()


@assert_stdout_matches('responses/ecommerce_sources.txt')
@intercept_requests('requests/ecommerce_sources.txt', generate=False)
# @write_stdout('responses/ecommerce_sources.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'ecommerce_sources')])
def test_ecommerce_sources():
    tap_google_analytics.main()


@assert_stdout_matches('responses/ecommerce_report.txt')
@intercept_requests('requests/ecommerce_report.txt', generate=False)
# @write_stdout('responses/ecommerce_report.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'ecommerce_report')])
def test_ecommerce_report():
    tap_google_analytics.main()


@assert_stdout_matches('responses/coupon_report.txt')
@intercept_requests('requests/coupon_report.txt', generate=False)
# @write_stdout('responses/coupon_report.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'coupon_report')])
def test_coupon_report():
    tap_google_analytics.main()


@assert_stdout_matches('responses/ecommerce_landing_report.txt')
@intercept_requests('requests/ecommerce_landing_report.txt', generate=False)
# @write_stdout('responses/ecommerce_landing_report.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('all-streams.json', 'ecommerce_landing_report')])
def test_ecommerce_landing_report():
    tap_google_analytics.main()