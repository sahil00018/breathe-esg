import pandas as pd

from ingestion.models import RawRecord
from emissions.services.normalizer import EmissionNormalizer


def process_uploaded_csv(data_source):

    file_path = data_source.uploaded_file.path

    df = pd.read_csv(file_path)

    normalizer = EmissionNormalizer()

    for _, row in df.iterrows():

        raw = RawRecord.objects.create(
            data_source=data_source,
            raw_data=row.to_dict(),
            status="PENDING"
        )

        normalizer.normalize_raw_record(
            raw,
            data_source.organization
        )