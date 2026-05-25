from datetime import datetime

from emissions.models import NormalizedEmissionRecord


class EmissionNormalizer:

    GALLON_TO_LITER = 3.785

    def normalize_unit(self, quantity, unit):

        if unit.lower() == "gallons":
            return quantity * self.GALLON_TO_LITER, "Liters"

        return quantity, unit


    def normalize_date(self, date_str):

        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y"
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).date()
            except:
                continue

        return None


    def map_scope(self, fuel_type):

        fuel_type = fuel_type.lower()

        if fuel_type in ["diesel", "petrol", "gasoline"]:
            return "SCOPE_1"

        return "UNKNOWN"


    def estimate_co2(self, fuel_type, quantity_liters):

        if fuel_type.lower() == "diesel":
            return quantity_liters * 2.68

        if fuel_type.lower() == "petrol":
            return quantity_liters * 2.31

        return None


    def normalize_raw_record(self, raw_record, organization):

        data = raw_record.raw_data

        quantity, unit = self.normalize_unit(
            float(data["quantity"]),
            data["unit"]
        )

        activity_date = self.normalize_date(data["date"])
        scope = self.map_scope(data["fuel_type"])
        co2 = self.estimate_co2(data["fuel_type"], quantity)

        record = NormalizedEmissionRecord.objects.create(
            organization=organization,
            raw_record=raw_record,
            scope=scope,
            category=data["fuel_type"],
            activity_date=activity_date,
            quantity=float(data["quantity"]),
            unit=data["unit"],
            normalized_quantity=quantity,
            normalized_unit=unit,
            co2e=co2,
            status="PENDING"
        )

        raw_record.status = "PROCESSED"
        raw_record.save()

        return record