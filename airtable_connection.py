from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

from pyairtable import Api, Table
from pyairtable.api.types import RecordDict, RecordDeletedDict

class AirtableConnection(ExperimentalBaseConnection[Api]):
    def _connect(self, **kwargs) -> Api:
        if 'access_token' in kwargs:
            access_token = kwargs.pop('access_token')
        else:
            access_token = self._secrets['access_token'] 
        return Api(access_token)

    
    def get_all(self, base_id, table_name, ttl: int = 3600) -> List[RecordDict]:
        @cache_data(ttl=ttl)
        def _getAll(base_id, table_name):
            table = self._instance().table(base_id, table_name)
            records = table.all()
            return records

        return _getAll(base_id, table_name)

    def get(self, base_id, table_name, record_id, ttl: int = 3600) -> RecordDict:
        @cache_data(ttl=ttl)
        def _get(base_id, table_name, record_id):
            table = self._instance().table(base_id, table_name)
            record = table.get(record_id)
            return record

        return _get(base_id, table_name)


    def create(self, base_id, table_name, record) -> RecordDict:
        table = self._instance().table(base_id, table_name)
        record = table.create(record)
        return record

    def create_many(self, base_id, table_name, records) -> List[RecordDict]:
        table = self._instance().table(base_id, table_name)
        records = table.batch_create(records)
        return records

    def update(self, base_id, table_name, record_id, fields, replace=False) -> RecordDict:
        table = self._instance().table(base_id, table_name)
        record = table.update(record_id, fields, replace=replace)
        return record

    def update_many(self, base_id, table_name, records, replace=False) -> List[RecordDict]:
        table = self._instance().table(base_id, table_name)
        records = table.batch_update(records, replace=replace)
        return records

    def delete(self, base_id, table_name, record_id) -> RecordDeletedDict:
        table = self._instance().table(base_id, table_name)
        record = table.delete(record_id)
        return record

    def delete_many(self, base_id, table_name, records) -> List[RecordDeletedDict]:
        table = self._instance().table(base_id, table_name)
        records = table.batch_delete(records)
        return records
        
