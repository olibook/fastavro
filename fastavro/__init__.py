'''Fast Avro file iteration.

Most of the code here is ripped off the Python avro package. It's missing a lot
of features in order to get speed.

The only onterface function is iter_avro, example usage::

    # Reading
    import fastavro as avro

    with open('some-file.avro', 'rb') as fo:
        reader = fastavro.reader(fo)
        schema = reader.schema

        for record in reader:
            process_record(record)


    # Writing
    from fastavro import writer

    schema = {
        'doc': 'A weather reading.',
        'name': 'Weather',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'station', 'type': 'string'},
            {'name': 'time', 'type': 'long'},
            {'name': 'temp', 'type': 'int'},
        ],
    }

    # 'records' can be an iterable (including generator)
    records = [
        {u'station': u'011990-99999', u'temp': 0, u'time': 1433269388},
        {u'station': u'011990-99999', u'temp': 22, u'time': 1433270389},
        {u'station': u'011990-99999', u'temp': -11, u'time': 1433273379},
        {u'station': u'012650-99999', u'temp': 111, u'time': 1433275478},
    ]

    with open('weather.avro', 'wb') as out:
        writer(out, schema, records)
'''

__version_info__ = (0, 17, 0)
__version__ = '%s.%s.%s' % __version_info__


import fastavro.read
import fastavro.write
import fastavro.schema


def _acquaint_schema(schema):
    """Add a new schema to the schema repo.

    Parameters
    ----------
    schema: dict
        Schema to add to repo
    """
    fastavro.read.acquaint_schema(schema)
    fastavro.write.acquaint_schema(schema)


reader = iter_avro = fastavro.read.iter_avro
schemaless_reader = fastavro.read.schemaless_reader
load = fastavro.read.read_data
writer = fastavro.write.writer
schemaless_writer = fastavro.write.schemaless_writer
dump = fastavro.write.dump
acquaint_schema = fastavro.schema.acquaint_schema
acquaint_schema = _acquaint_schema
fastavro.schema.acquaint_schema = _acquaint_schema
is_avro = fastavro.read.is_avro

__all__ = [
    n for n in locals().keys() if not n.startswith('_')
] + ['__version__']
