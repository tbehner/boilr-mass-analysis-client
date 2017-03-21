"""{{AnalysisName | title}} Analysis System

{{Description}}
"""
import sys
import time
import logging
import configparser
from mass_client import AnalysisClient
from mass_api_client import resources
from common_helper_files import update_config_from_env

logging.basicConfig()
log = logging.getLogger('{{AnalysisName | toLower}}_analysis_system')
log.setLevel(logging.INFO)

class {{AnalysisName | title}}AnalysisInstance(AnalysisClient):
    def __init__(self, **kwargs):
        # TODO put your initialization here
        super().__init__(**kwargs)

    def analyze(self, scheduled_analysis):
        sample = scheduled_analysis.get_sample()

        self.submit_report(
            scheduled_analysis,
            json_report_objects={'{{AnalysisName | toLower}}_report': {}},
            )


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    update_config_from_env(config)
    {{AnalysisName | toTitle}}AnalysisInstance.create_from_config(config).start()
