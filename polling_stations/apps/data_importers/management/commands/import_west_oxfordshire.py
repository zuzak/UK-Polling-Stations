from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "WOX"
    addresses_name = "2021-03-15T11:16:34.226362/WODC - EC & Democracy Club Polling Place Look Up for 6 May 2021 (Rev).csv"
    stations_name = "2021-03-15T11:16:34.226362/WODC - EC & Democracy Club Polling Place Look Up for 6 May 2021 (Rev).csv"
    elections = ["2021-05-06"]

    def station_record_to_dict(self, record):

        # Brize Norton Elder Bank Hall
        if record.polling_place_id == "7318":
            record = record._replace(polling_place_postcode="OX18 3PU")
            record = record._replace(polling_place_easting="430059")
            record = record._replace(polling_place_northing="207340")

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        if record.addressline6 in ["OX28 6DH"]:
            return None  # split

        if record.addressline6 in ["GL56 0SU"]:
            return None  # spurious

        return super().address_record_to_dict(record)
