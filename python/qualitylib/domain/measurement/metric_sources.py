'''
Copyright 2012-2015 Ministerie van Sociale Zaken en Werkgelegenheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


class MetricSources(dict):

    def __init__(self, keys_and_values):
        new_keys_and_values = {key: MetricSources.__ensureList(key, value) for key, value in keys_and_values.items()}
        super(MetricSources, self).__init__(new_keys_and_values)

    @staticmethod
    def __ensureList(key, value):
        if hasattr(key, 'needs_values_as_list') and key.needs_values_as_list and type(value) != type([]):
            return [value]
        return value