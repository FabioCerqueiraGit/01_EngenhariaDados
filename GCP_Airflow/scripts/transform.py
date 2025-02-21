import apache_beam as beam
import json
from apache_beam.options.pipeline_options import PipelineOptions

class TransformData(beam.DoFn):
    def process(self, element):
        record = json.loads(element)
        record['total_price'] = record['price'] * record['quantity']
        yield record

if __name__ == '__main__':
    pipeline_options = PipelineOptions()
    
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | 'Read from GCS' >> beam.io.ReadFromText('gs://meu-bucket-de-dados/raw/sample_data_large.json')
            | 'Transform Data' >> beam.ParDo(TransformData())
            | 'Write to GCS' >> beam.io.WriteToText('gs://meu-bucket-de-dados/processed/sample_data_transformed', file_name_suffix='.json')
        )
